class PizzaAI:
    def __init__(self):
        self.pizza_dict = {
         		'cheese': 'For a Cheese pizza, you need dough, tomato sauce, and fresh mozzarella cheese',
            'margherita': 'For a Margherita pizza, you need dough, tomato sauce, fresh mozzarella, and basil.',
            'pepperoni': 'To make Pepperoni pizza, gather dough, tomato sauce, mozzarella cheese, and pepperoni slices.',
            'vegetarian': 'For a Vegetarian pizza, you can use dough, tomato sauce, mozzarella, and assorted veggies like bell peppers, onions, and mushrooms.',
          	'brain': 'For a brain pizza, you need ligaments, guts, and freshly sliced brain'
        }

    def answer_question(self, question):
        for pizza_type, ingredients in self.pizza_dict.items():
            if pizza_type in question.lower():
                return ingredients
        return "I'm not sure how to make that kind of pizza."

if __name__ == "__main__":
    pizza_ai = PizzaAI()

    while True:
        user_input = input("Ask me how to make a pizza (type 'exit' to end): ")
        
        if user_input.lower() == 'exit':
            break

        response = pizza_ai.answer_question(user_input)
        print(response)