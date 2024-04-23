
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
        })
    })

    beforeEach(function () {
        cy.visit('http://localhost:3000')
        cy.contains('div', 'Email Address')
            .find('input[type=text]')
            .type(email)

        cy.get('form')
            .submit()

        cy.get('h1')
            .should('contain.text', 'Your tasks, ' + name)
    })

    it('Finding form and adding one task without text', () => {
        cy.get('form')
            .should('contain.text', 'Title')

        cy.get('form')
            .find('input[type=submit]')
            .should("be.disabled")
    })

    it('Finding form and adding one task', () => {
        cy.get('form')
            .should('contain.text', 'Title')

        cy.contains('div', 'Title')
            .find('input[type=text]')
            .type(task)

        cy.get('form')
            .submit()
        
        cy.get('p')
            .should('contain.text', 'Here you can find your 1 task. Click on each thumbnail in the list to add, update, or delete the todo items you have associated to this video.')
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