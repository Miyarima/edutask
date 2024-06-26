
describe ("Add task to todo list", () => {

    let uid // user id
    let name // name of the user (firstName + ' ' + lastName)
    let email // email of the user
    let todo_id // the id of todo items
    const task = "this is the first task"

    before(function () {
        cy.fixture('tasksUser.json')
            .then((user) => {
            cy.request({
                method: 'POST',
                url: 'http://localhost:5000/users/create',
                form: true,
                body: user
            }).then((response) => {
                uid = response.body._id.$oid
                name = user.firstName + ' ' + user.lastName
                email = user.email
            })
            .then(() => {
                cy.visit('http://localhost:3000')
                cy.contains('div', 'Email Address')
                    .find('input[type=text]')
                    .type(email)
        
                cy.get('form')
                    .submit()
        
                cy.get('h1')
                    .should('contain.text', 'Your tasks, ' + name)
                
                cy.get('form')
                    .should('contain.text', 'Title')
        
                cy.contains('div', 'Title')
                    .find('input[type=text]')
                    .type(task)
        
                cy.get('form')
                    .submit()
                
                cy.get('p')
                    .should('contain.text', 'Click on each thumbnail in the list to add, update, or delete the todo items you have associated to this video.')
            })
            .then(() => {
                cy.request({
                        method: 'GET',
                        url: `http://localhost:5000/tasks/ofuser/${uid}`
                    }).then((response) => {
                        cy.log(response)
                        todo_id = response.body[0].todos[0]._id.$oid
                })
            })
        })
    })

    beforeEach(function () {
        cy.visit('http://localhost:3000')
        cy.contains('div', 'Email Address')
            .find('input[type=text]')
            .type(email);

        cy.get('form')
            .submit();

        cy.wait(3000)

        cy.contains("div", "a")
            .click();
    })

    it('check if todo item is unchecked', () => {
        cy.contains('.todo-item', 'Watch video')
                .find('.unchecked')
                .should("have.class", "unchecked");

    })

    it('Set an todo as done', () => {
        cy.fixture("todo_done.json").then((todo) => {
            cy.request({
                method: 'PUT',
                url: `http://localhost:5000/todos/byid/${todo_id}`,
                form: true,
                body: todo
            })
        })
    })

    it('Check if todo item is checked', () => {
        cy.contains('.todo-item', 'Watch video')
            .find('.checked')
            .should("have.class", "checked");

    })

    it('Remove added item in todo list', () => {
        cy.contains('.todo-item', 'Watch video')
            .find('.remover')
            .last()
            .click();
    
        cy.get(".todo-list")
            .children()
            .should("have.length", 1);
    })

    
    after(function () {
        // clean up by deleting the user from the database
        cy.request({
            method: 'DELETE',
            url: `http://localhost:5000/users/${uid}`
            }).then((response) => {
            cy.log(response.body)
        })
    })
})
