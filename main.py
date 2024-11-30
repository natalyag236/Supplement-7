import matplotlib.pyplot as plt

def test_plot_stress_vs_strain():
    strain = [0.5, 0.916, 0.72, 0.229] 
    stress = [234076.43, 421337.57, 25995.33, 9358.31] 
    plt.plot(strain, stress, label="Stress vs Strain", marker='o')
    plt.xlabel("Strain")
    plt.ylabel("Stress (N/m²)")
    plt.title("Stress vs Strain Graph")

    plt.grid(True)


    plt.legend()


    plt.show()


test_plot_stress_vs_strain()
