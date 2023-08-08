import matplotlib.pyplot as plt
import matplotlib.patches as patches

def find_slope(x1, y1, x2, y2):
    # Avoid division by zero
    if x2 - x1 == 0:
        return float('inf')
    return (y2 - y1) / (x2 - x1)

def find_orthocenter(x1, y1, x2, y2, x3, y3):
    # Step 1: Calculate the slopes of the sides of the triangle ABC
    mAB = find_slope(x1, y1, x2, y2)
    mBC = find_slope(x2, y2, x3, y3)

    # Step 2: Using the slopes of the sides of a triangle, find the slopes of altitudes.
    if mAB == 0:  # Handle the case when the slope is zero
        mCF = 0
    else:
        mCF = -1 / mAB

    if mBC == 0:  # Handle the case when the slope is zero
        mAD = 0
    else:
        mAD = -1 / mBC

    # Step 3: With the help of the point-slope form equation, find the equations of the altitudes
    # Using the point-slope form: y - y1 = m(x - x1)
    # Equation of CF: y - y3 = mCF(x - x3)
    # Equation of AD: y - y1 = mAD(x - x1)

    # Step 4: Solve the equations of any two altitudes to find the orthocenter
    # Equating the two equations to find x:
    # mCF(x - x3) + y3 = mAD(x - x1) + y1
    x = (y1 - y3 + mCF * x3 - mAD * x1) / (mCF - mAD)
    y = mCF * (x - x3) + y3

    return x, y

def find_distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def draw_triangle_and_circle(A, B, C):
    # Step 1: Find the orthocenter
    orthocenter = find_orthocenter(A[0], A[1], B[0], B[1], C[0], C[1])
    radius = find_distance(orthocenter[0], orthocenter[1], A[0], A[1])
    print('Orthocenter:', orthocenter)
    print('Radius:', radius)
    print('x^2 + y^2 +', -2*orthocenter[0], 'x +', -2*orthocenter[1], 'y +', orthocenter[0]*2 + orthocenter[1]*2 - radius**2, '= 0')
    
    # Plotting the triangle
    plt.plot([A[0], B[0]], [A[1], B[1]], 'b-')
    plt.plot([B[0], C[0]], [B[1], C[1]], 'b-')
    plt.plot([A[0], C[0]], [A[1], C[1]], 'b-')

    # Plotting the vertices
    plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='blue', label='Vertices')
    
    # Plotting the orthocenter
    plt.scatter(orthocenter[0], orthocenter[1], color='red', label='Orthocenter')

    # Drawing the circle with orthocenter as center
    circle = patches.Circle(orthocenter, radius, fill=False, color='green', linestyle='dotted', label='Circle')
    plt.gca().add_patch(circle)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Triangle with Orthocenter and Circle')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')  # Ensures the scale is the same on both axes
    plt.show()


draw_triangle_and_circle([1,-1],[-4,6],[-3,-5])
