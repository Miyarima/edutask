
describe ("Add task to todo list", () => {

    let uid // user id
    let name // name of the user (firstName + ' ' + lastName)
    let email // email of the user
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

    it('Add new todo without text', () => {
        cy.get('.inline-form')
            .find('input[type=text]')
            .clear({ force: true })
        cy.get('.inline-form')
            .find('input[type=submit]')
            .should("be.disabled");
    })

    it('Add new todo with text', () => {
        cy.get('.inline-form')
            .find('input[type=text]')
            .type("customer meeting at 1");
        
        cy.get('.inline-form')
            .submit();
        
        cy.get('.todo-list')
            .should("contain.text", "customer meeting at 1");
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
