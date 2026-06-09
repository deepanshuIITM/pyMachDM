### Solution Comparison 

### **Inter-objective Class Comparison**

$\mathcal{M}_{PE} = \max_{m=1}^{M} (3-I_m)$

### **Intra-objective Class Comparison**

$\max \big(\bar{z}_i^n, \varepsilon_j^n  \big),\ 
    \forall i \in \textbf{I}^{\leq}, \forall j \in \textbf{I}^{\geq}$

### **$\mathcal{M}_{PE}$ Metric**

$\mathcal{M}_{PE} = \max_{m=1}^{M} (3-I_m) + \left\{\max \big(\bar{z}_i^n, \varepsilon_j^n  \big),\ 
    \forall i \in \textbf{I}^{\leq}, \forall j \in \textbf{I}^{\geq}\right\}$

The values of $\bar{z}_i^n$ and $\varepsilon_j^n$ are obtained by normalizing the bounding parameters $\varepsilon_j$ and $\bar{z}_i$ between 0 and 1, with respect to the target point $\mathbf{f}^T$, as follows:


$\bar{z}_i^n = \dfrac{\bar{z}_i -  f_i^T}{f_i^R - f_i^T}$,  $\varepsilon_j^n = \dfrac{f_j^T - \varepsilon_j}{f_j^T - f_j^{\ast}}$
