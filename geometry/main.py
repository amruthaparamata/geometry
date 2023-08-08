import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_triangle_and_circle(A, B, C):
    orthocenter = (17/6,5/6)
    radius = (8.59)

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

# Example usage:
A = ( 1,-1)
B = (-4, 6)
C = (-3,-5)
draw_triangle_and_circle(A, B, C)
