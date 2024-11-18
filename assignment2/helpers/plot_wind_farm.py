import numpy as np
import matplotlib.pyplot as plt

def add_wind_rose(ax, wind, inset_position=[1.1, 0.45, 0.32, 0.32]):
    """
    Add a wind rose inset to the current axes.

    Parameters:
    - ax: Current matplotlib axes.
    - wind: The wind vector [u, v] as a 2D array-like object.
    - inset_position: Position of the inset as [left, bottom, width, height].
    """
    # Compute angle and normalized magnitude of wind (to fit within the wind rose)
    wind_angle = np.arctan2(wind[1], wind[0])  # Angle in radians
    max_wind_strength = 30  # Maximum wind strength in m/s
    wind_magnitude = np.linalg.norm(wind)
    normalized_magnitude = min(wind_magnitude / max_wind_strength, 1.0)  # Scale and then clamp to [0, 1]

    # Create inset axes for the wind rose
    inset_ax = ax.inset_axes(inset_position, polar=True)
    inset_ax.grid(zorder=1)
    
    # Configure the wind rose plot
    inset_ax.set_theta_zero_location("N")
    inset_ax.set_theta_direction(-1)  # Clockwise
    inset_ax.set_yticklabels([])  # Hide radial ticks
    inset_ax.set_ylim(0, 1)  # Normalize wind strength

    # Add a title to the wind rose with wind angle and magnitude
    inset_ax.text(
        0.5, 1.3, f"Wind Rose for w=({wind[0]:.1f}, {wind[1]:.1f})\nWind Angle: {np.degrees(wind_angle):.1f}°\nWind Speed: {wind_magnitude:.2f} m/s",
        horizontalalignment="center", verticalalignment="center",
        transform=inset_ax.transAxes, fontsize=12
    )

    # Add an arrow representing the wind
    if normalized_magnitude > 0:
        inset_ax.quiver(
            0, 0, normalized_magnitude*np.cos(wind_angle), normalized_magnitude*np.sin(wind_angle),
            # angles='xy', scale=1, scale_units='xy',
            scale=2/(normalized_magnitude),
            color="green",
            width=0.02,
            headwidth=3, headlength=4.5,
            zorder=2
        )

def plot_wind_farm(instance, selected_turbines, wind=None, **kwargs):
    """
    Plot the wind farm layout with the selected turbine sites and exclusion zones.

    Parameters:
    - instance: The wind farm instance dictionary.
    - selected_turbines: A list of indices of the selected turbine sites.
    - wind: The wind vector [u, v] as a 2D array-like object.
    """
    coords = instance["coords"]
    min_distance = instance["min_distance"]

    _, ax = plt.subplots(figsize=[10, 10])

    # Plot the site locations
    ax.scatter(coords[:, 0], coords[:, 1], s=100, label="Sites")

    # Annotate site indices
    for idx in range(len(coords)):
        margin = 0.08
        ax.annotate(idx, (coords[idx, 0] + margin, coords[idx, 1] + margin))

    # Plot turbine locations
    turbine_coords = coords[selected_turbines]
    ax.scatter(*turbine_coords.T, s=100, label="Turbines")

    # Draw exclusion zones around turbines
    for (x, y) in turbine_coords:
        cir = plt.Circle((x, y), min_distance, color="r", alpha=0.08, label="Exclusion zones")
        ax.add_patch(cir)

    # Avoid duplicate legend entries for the exclusion zones
    handles, labels = ax.get_legend_handles_labels()
    unique_handles_labels = {label: handle for handle, label in zip(handles, labels)}
    ax.legend(unique_handles_labels.values(), unique_handles_labels.keys(), loc='lower left', bbox_to_anchor=(1.07, 0.15), fontsize=12)

    # Configure plot limits
    x_min, x_max = coords[:, 0].min() - 1.3, coords[:, 0].max() + 1.3
    y_min, y_max = coords[:, 1].min() - 1.3, coords[:, 1].max() + 1.3
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_aspect('equal')  # Ensure equal aspect ratio
    ax.set_xticks(np.arange(0, 6, 1))
    ax.set_yticks(np.arange(0, 6, 1))

    # Add wind rose if wind vector is provided
    if wind is not None:
        add_wind_rose(ax, wind)
    ax.set_title(f"Wind farm layout with {selected_turbines} as selected turbine sites\n")

    plt.tight_layout()
    plt.show()
