from scipy import misc


def f(x):
    return 4*x ** 3 - 48*x + 5


# Finding roots using the Newton Rapson method
def newton(x0, x1, epsilon):
    min_section = x0
    max_section = x1
    xn = x0
    iter = 0

    while True:
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print(f"Section [{min_section} ,{max_section}]: Found solution after {iter} iterations: {xn}")
            break
        Dfxn = misc.derivative(f, xn)
        if Dfxn == 0:
            print("Zero derivative. No solution found.")
            break
        xn = xn - fxn/Dfxn
        iter += 1


# Finding roots using the secant method
def secant(x0, x1, e):
    min_section = x0
    max_section = x1
    iter = 1
    condition = True

    while condition:
        if f(x0) == f(x1):
            print("Divide by zero error!")
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        iter += 1

        condition = abs(f(x2)) > e
    print(f"Section [{min_section} ,{max_section}]: Found solution after {iter} iterations: {x2}")


if __name__ == "__main__":
    epsilon = 0.0001

    min_range = int(input("Please enter min range: "))
    max_range = int(input("Please enter max range: "))
    newton_section_list = []
    secant_section_list = []

    # Check if there is a root in a certain value range (in increments of 1)
    for i in range(min_range, max_range):
        if f(i) * f(i + 1) < 0:
            newton_section_list.append((i, i + 1))
            secant_section_list.append((i, i + 1))

    # Finding roots by Newton Raphson method:
    print("-------------------------")
    print("Roots by Newton Raphson method:")
    print("-------------------------")

    # Sending X0 for which a root approximation is found
    if len(newton_section_list) == 0:
        print("No roots were found using a Newton Raphson method")
    else:
        for section in newton_section_list:
            newton(section[0], section[1], epsilon)

    # Finding roots by secant method:
    print("-------------------------")
    print("Roots by secant method:")
    print("-------------------------")

    # Sending 2 X0 and X1 guesses for possible ranges for finding roots
    if len(secant_section_list) == 0:
        print("No roots were found using a secant method")
    else:
        for section in secant_section_list:
            secant(section[0], section[1], epsilon)

