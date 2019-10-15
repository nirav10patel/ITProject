def main():
    str = "catBatSatFatOr"
    data = [str[i:i+3] for i in range(0, len(str), 3)]
    for i in range(0, 5):
        print(data[i])

if __name__ == "__main__":
    main()
