# Caroline Rutendo Nyamupanda
# R00205878

def information():
    destination = input("What town are you going to? ")
    distance = ""
    distance = float(input(f"How far is {destination}?"))

    return destination, distance


def process_information():
    distance = []
    destination = []
    if destination <= 15:
        estimation = distance * 0.067
        walking = float(input(f"you should walk {estimation} hours"))

    else:
        cycle_estimation = distance * 0.2
        suggestion = float(input(f"You should cycle in {cycle_estimation} hours"))

    return walking, suggestion


def main():
    destination, distance = information()
    walking, suggestion = process_information()


if __name__ == '__main__':
    main()
