The :defterm[$q$-von Mangoldt function]{#q-von-mangoldt-function} is defined over the maximal ideals
$\mathfrak{m}$ of the coordinate ring $\mathcal{O}_q(\mathcal{B})$. For a
maximal ideal $\mathfrak{m}$ with norm $N(\mathfrak{m})$ (the cardinality
of the residue field):

$$
\Lambda_q(\mathfrak{m}) = \begin{cases}
\dfrac{N(\mathfrak{m})^{\hbar_q} - 1}{\hbar_q} & \text{if } \mathfrak{m} \text{ corresponds to a fundamental defect}, \\[6pt]
0 & \text{otherwise}.
\end{cases}
$$

A maximal ideal is a **fundamental defect** if it lies over a prime ideal
of the center of $A$. The weight
$\frac{N(\mathfrak{m})^{\hbar_q} - 1}{\hbar_q}$ is the $q$-deformation of
$\log N(\mathfrak{m})$: as $q \to 1$ (hence $\hbar_q \to 0$), L'Hôpital's
rule gives $\Lambda_q(\mathfrak{m}) \to \log N(\mathfrak{m}) = \Lambda(\mathfrak{m})$, the classical von Mangoldt function.
