def main():
    english_units_conversions = 703
    for height in range(54, 83, 2):
        print('Current heights:', height)
        for weight in range(85, 351, 5):
            bmi = english_units_conversions * weight / (height ** 2)

            print('height =', height, 'weight =', weight,
                  'bmi =', format(bmi, '<4.1f'))

main()