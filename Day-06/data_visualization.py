import matplotlib.pyplot as plt

def create_line_chart():
    """Creates a basic line chart."""
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 12, 9]

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Sales')
    plt.title('Line Chart: Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Sales (in units)')
    plt.grid(True)
    plt.legend()
    # Save the chart as an image
    plt.savefig('line_chart.png')
    plt.show()

def create_bar_chart():
    """Creates a basic bar chart."""
    categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
    values = [25, 40, 15, 30]

    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color='orange')
    plt.title('Bar Chart: Fruit Inventory')
    plt.xlabel('Fruit Type')
    plt.ylabel('Quantity')
    # Save the chart as an image
    plt.savefig('bar_chart.png')
    plt.show()

def create_scatter_plot():
    """Creates a basic scatter plot."""
    height = [150, 160, 165, 170, 175, 180, 185]
    weight = [50, 55, 60, 65, 70, 75, 80]

    plt.figure(figsize=(8, 5))
    plt.scatter(height, weight, color='green', marker='x')
    plt.title('Scatter Plot: Height vs Weight')
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    plt.grid(True)
    # Save the chart as an image
    plt.savefig('scatter_plot.png')
    plt.show()

if __name__ == '__main__':
    print("Generating Line Chart...")
    create_line_chart()
    
    print("Generating Bar Chart...")
    create_bar_chart()
    
    print("Generating Scatter Plot...")
    create_scatter_plot()
    print("All charts have been created and saved as PNG files.")
