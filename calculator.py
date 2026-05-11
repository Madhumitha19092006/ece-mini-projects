# ECE Mini Projects Repository Pack

## Repository Name

`ece-mini-projects`

---

# README.md

```md
# ECE Mini Projects

A collection of simple Electronics and Communication Engineering mini projects using Python and MATLAB.

## Technologies Used
- Python
- MATLAB
- NumPy
- Matplotlib

## Projects Included
1. ASK Modulation
2. FSK Modulation
3. PSK Modulation
4. Factorial Program
5. Simple Calculator

## Author
Madhu
```

---

# Project 1: Python Calculator

## File: calculator.py

```python
print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Result =", num1 + num2)
elif choice == 2:
    print("Result =", num1 - num2)
elif choice == 3:
    print("Result =", num1 * num2)
elif choice == 4:
    print("Result =", num1 / num2)
else:
    print("Invalid Choice")
```

---

# Project 2: Factorial Program

## File: factorial.py

```python
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)
```

---

# Project 3: ASK Modulation MATLAB

## File: ask_modulation.m

```matlab
clc;
clear all;
close all;

x = [1 0 1 1 0 1];
bitrate = 1;
T = length(x);
nb = 100;

for i = 1:T
    if x(i) == 1
        y((i-1)*nb+1:i*nb) = sin(2*pi*5*(0:nb-1)/nb);
    else
        y((i-1)*nb+1:i*nb) = 0;
    end
end

plot(y);
title('ASK Modulation');
```

---

# Project 4: FSK Modulation MATLAB

## File: fsk_modulation.m

```matlab
clc;
clear all;
close all;

x = [1 0 1 0 1];
nb = 100;

for i = 1:length(x)
    if x(i) == 1
        y((i-1)*nb+1:i*nb) = sin(2*pi*10*(0:nb-1)/nb);
    else
        y((i-1)*nb+1:i*nb) = sin(2*pi*5*(0:nb-1)/nb);
    end
end

plot(y);
title('FSK Modulation');
```

---

# Project 5: PSK Modulation MATLAB

## File: psk_modulation.m

```matlab
clc;
clear all;
close all;

x = [1 0 1 1 0];
nb = 100;

for i = 1:length(x)
    if x(i) == 1
        y((i-1)*nb+1:i*nb) = sin(2*pi*5*(0:nb-1)/nb);
    else
        y((i-1)*nb+1:i*nb) = sin(2*pi*5*(0:nb-1)/nb + pi);
    end
end

plot(y);
title('PSK Modulation');
```

---

# How to Upload to GitHub

1. Create a new repository named `ece-mini-projects`
2. Upload all files
3. Add README.md
4. Commit changes
5. Make repository public

---

# Suggested GitHub Description

`ECE mini projects using Python and MATLAB for communication systems and basic programming.`

---

# Suggested Topics

`python`
`matlab`
`ece`
`communication-systems`
`mini-projects`
`engineering`
