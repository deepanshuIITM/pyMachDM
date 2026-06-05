## Multi-objective Optimization

* **Core Concept:** Optimization of multiple, mutually conflicting objective functions simultaneously where no single optimal solution exists.
* **Goal:** To identify the "Pareto optimal" set—solutions where one objective cannot be improved without degrading another.
## Mathematical Formulation

$$
\begin{aligned}
\text{minimize} \quad & \mathbf{f}(\mathbf{x}) = \left( f_1(\mathbf{x}), f_2(\mathbf{x}), \dots, f_m(\mathbf{x}) \right)^T \\
\text{subject to} \quad & g_i(\mathbf{x}) \le 0, \quad i = 1, 2, \dots, p \\
& h_j(\mathbf{x}) = 0, \quad j = 1, 2, \dots, q \\
& \mathbf{x} \in \mathcal{S}
\end{aligned}
$$

where- 

* **$\mathbf{x}$:** The $n$-dimensional decision variable vector within the feasible space $\mathcal{S}$.
* **$\mathbf{f}(\mathbf{x})$:** The objective vector representing $m$ distinct criteria ($m \ge 2$).
* **$g_i(\mathbf{x}), h_j(\mathbf{x})$:** The inequality and equality constraints mapping system boundaries.

---


## Multi-Criterion Decision-making

* **A Priori Methods:** Preferences, goals, or hard constraints are explicitly specified by the user *before* running the optimization routine.
* **A Posteriori Methods:** The algorithm generates a wide array of Pareto-optimal trade-offs first; the user selects the final operating design *afterward*.
* **Interactive Methods:** A tight, real-time loop where the system generates candidate options, the user gives feedback, and the algorithm continuously adapts its search path.

---

## Interactive Visualization

* **Core Purpose:** Serves as the interactive cognitive interface enabling users to interpret complex, high-dimensional trade-off spaces.
* **Parallel Coordinates Plots:** Maps highly dimensional parameters along vertical parallel axes, allowing real-time filtering of solution pathways.
* **Scatter Plot Matrices (Brushing & Linking):** Linking interactive charts so selecting data points on an objective trade-off front highlights its physical decision variables everywhere else instantly.
