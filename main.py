def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = 23

    fahrenheit = celcius * 9/5 + 32

    print(f"{celcius:.2f} Celsius is equal to {fahrenheit:.2f} Fahrenheit")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
