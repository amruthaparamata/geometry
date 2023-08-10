import matplotlib.pyplot as plt
import matplotlib.patches as patches

def findCircumCenter(A, B, C):
    # D is midpoint of BC
    D = midPoint(B, C)
    # E is midpoint of AC
    E = midPoint(A, C)
    # F is midpoint of AB
    F = midPoint(A, B)
    # Slope of AB
    
    m1 = slope(A, B)
    # Slope of BC
    m2 = slope(B, C)
    # Slope of AC
    m3 = slope(A, C)
    # Slope of perpendicular to AB
    m4 = -1 / m1
    # Slope of perpendicular to BC
    m5 = -1 / m2
    # Slope of perpendicular to AC
    m6 = -1 / m3
    # equation of perpendicular bisector of AB
    # y - y1 = m4(x - x1)
    # y = m4x - m4x1 + y1
    a1 = m4
    b1 = -m4 * F[0] + F[1]
    # equation of perpendicular bisector of BC
    # y - y2 = m5(x - x2)
    # y = m5x - m5x2 + y2
    a2 = m5
    b2 = -m5 * D[0] + D[1]
    # intersection of perpendicular bisector of AB and BC
    # a1x + b1 = a2x + b2
    # x = (b2 - b1) / (a1 - a2)
    x = (b2 - b1) / (a1 - a2)
    # y = a1x + b1
    y = a1 * x + b1
    return [x, y]


def slope(A, B):
    return (B[1] - A[1]) / (B[0] - A[0])

def midPoint(A, B):
    return [(A[0] + B[0]) / 2, (A[1] + B[1]) / 2]

def draw_triangle_and_circle(A, B, C):
    circumcenter = findCircumCenter(A, B, C)
    radius = ((A[0] - circumcenter[0])**2 + (A[1] - circumcenter[1])**2)**0.5
    print('Circumcenter:', circumcenter)
    print('Radius:', radius)
    print('Equation of the circle:')
    print('x^2 + y^2 +', -2 * circumcenter[0], 'x +', -2 * circumcenter[1], 'y +', circumcenter[0]**2 + circumcenter[1]**2 - radius**2, '= 0')
    # Plotting the triangle
    plt.plot([A[0], B[0]], [A[1], B[1]], 'b-')
    plt.plot([B[0], C[0]], [B[1], C[1]], 'b-')
    plt.plot([A[0], C[0]], [A[1], C[1]], 'b-')

    # Plotting the vertices
    plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='blue', label='Vertices')
    
    # Plotting the circumcenter
    plt.scatter(circumcenter[0], circumcenter[1], color='red', label='Circumcenter')

    # Drawing the circle with circumcenter as center
    circle = patches.Circle(circumcenter, radius, fill=False, color='green', linestyle='dotted', label='Circle')
    plt.gca().add_patch(circle)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Triangle with its Circumcircle')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')  # Ensures the scale is the same on both axes
    plt.show()


draw_triangle_and_circle([1,-1],[-4,6],[-3,-5])
