describe("try!", () => {
    it("do nothing", () => {
        expect(true).to.equal(true)
    })

    it.only("visit list product", () => {
        cy.wait(2000)
        cy.visit("localhost:5000")
        cy.wait(2000) })


        it.only("Test history button ", () => {
            cy.wait(1500)
            cy.get(':nth-child(1) > .text-right > [data-bind="click: $parent.EditHistory"]').click()
            cy.wait(2000)
            cy.get('.modal-content > .modal-header > .close > span').click()          
   
       })   
       
       it.only("Test products by category button", () => {
        cy.wait(1500)
        cy.get(':nth-child(2) > .nav-link').click()
        cy.wait(2000)
        cy.url().should('include', 'localhost:5000/categories')
        cy.wait(2000)
        cy.get(':nth-child(1) > .nav-link').click()
    })   
    it.only("Test products by category button", () => {
        cy.wait(1500)
        cy.get(':nth-child(1) > .text-right > [data-bind="click: $parent.EditPrice"]').click()
        cy.wait(2000)
        cy.get('#ActualPriceInput').clear().type('9')
        cy.wait(2000)
        cy.get('[type="submit"]').click()
        cy.get('form > .modal-footer > [type="button"]').click()
        
    })  
})