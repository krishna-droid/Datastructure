def draw_pyramid(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# Uncomment the line below to test the function
# draw_pyramid(5)
