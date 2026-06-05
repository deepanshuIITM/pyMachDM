### Weighted-sum

* **Mathematical Formulation:**

  $U(\mathbf{x}) = \sum\limits_{i=1}^{M} w_i f_i(\mathbf{x})$

* **Description:** Condenses multi-dimensional objectives into a single scalar score by multiplying each objective by an assigned weight ($w_i$). It is simple to compute but completely fails to identify or reach optimal solutions located in non-convex regions of the Pareto front.

### Tchebycheff

* **Mathematical Formulation:**

  $\text{minimize} \quad \max\limits_{i=1 \dots M} \left[ \dfrac{| f_i(\mathbf{x}) - z_i^* |}{w_i} \right]$

* **Description:** Minimizes the maximum weighted distance between a solution and a theoretical ideal reference point ($\mathbf{z}^*$). While it can find solutions along any non-convex Pareto shape, its strict geometric boundaries can occasionally yield weakly Pareto-optimal points.

### ASF 

* **Mathematical Formulation:**

  $\text{minimize} \quad \max\limits_{i=1 \dots M} \left[ \dfrac{f_i(\mathbf{x}) - \hat{z}_i}{z_i^{\rm nad}-z_i^{**}} \right]$

* **Description:** A flexible variation of the Tchebycheff metric that replaces the absolute ideal bounds with an arbitrary, user-defined aspiration target ($\mathbf{\hat{z}}$). If the target is unfeasible, it finds the closest available alternative; if the target is easily reached, it continues to optimize past it.

### AASF 

* **Mathematical Formulation:**

  $\text{minimize} \quad \max\limits_{i=1 \dots M} \left[ \dfrac{f_i(\mathbf{x}) - \hat{z}_i}{z_i^{\rm nad}-z_i^{**}} \right]+ \rho \sum\limits_{i=1}^{M} \left[ \dfrac{f_i(\mathbf{x})}{z_i^{\rm nad}-z_i^{**}} \right]$

* **Description:** Introduces a linear weighted sum regularization term to the primary ASF framework, scaled by a small positive augmentation parameter ($\rho > 0$). This addition mathematical eliminates edge anomalies, ensuring all generated trade-offs are strictly Pareto-optimal.