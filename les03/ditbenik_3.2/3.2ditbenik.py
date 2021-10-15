
def main():
    questions = [
        {
            'question': 'Hoe oud ben ik?',
            'answers': {
                'a': '16',
                'b': '17',
                'c': '18'
            },
            'right_answer': 'a'
        },
        {
            'question': 'Waar kom ik vandaan?',
            'answers': {
                'a': 'Amsterdam',
                'b': 'Purmerend',
                'c': 'Zaandam'
            },
            'right_answer': 'b'
        },
        {
            'question': 'wat is mijn favoriete eten',
            'answers': {
                'a': 'Pizza',
                'b': 'Burritos',
                'c': 'Kapsalon'
            },
            'right_answer': 'c'
        },
        {
            'question': 'In welke stad zat ik hiervoor op school?',
            'answers': {
                'a': 'Purmerend',
                'b': 'Zaandam',
                'c': 'Hoorn'
            },
            'right_answer': 'b'
        }
    ]
    points = 0

    def check_input(input_question, input_key) -> bool:
        return input_question['right_answer'] == input_key.lower() or input_question['answers'][
            input_question['right_answer']].lower() == input_key.lower()

    for question in questions:
        print(question['question'])
        print(len(question['question']) * '-')

        for answer in question['answers']:
            print(f"{answer.upper()} - {question['answers'][answer]}")

        correct = check_input(question, input('>> '))
        if correct:
            print('Goed!')
            points += 1
        else:
            print('fout!')

    print(f"Je hebt {points} van de {len(questions)} vragen juist beantwoord.")
    percentage = 100 / len(questions) * points
    print(f"Dat is {percentage}% van de vragen goed beantwoord.")


if __name__ == '__main__':
    main()