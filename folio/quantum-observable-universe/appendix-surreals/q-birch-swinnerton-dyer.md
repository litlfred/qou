**Conjecture ($q$-BSD).**
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU with substrate parameter $q$ and Descartes elliptic curve $\mathcal{E}_q$. Let $\mathcal{E}_q(\mathbf{1}) = \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, E_q)$ be the categorical Mordell--Weil group with rank $r_q = \mathrm{rank}\,\mathcal{E}_q(\mathbf{1})$. Let $L(\mathcal{E}_q, s)$ be the $q$-deformed $L$-function, and $\mathrm{Sha}_q(\mathcal{E}_q)$ the $q$-Tate--Shafarevich group ([categorical Mordell--Weil](#def:categorical-mordell-weil)). The conjecture has two parts, mirroring classical BSD:

**(Weak $q$-BSD).**
The order of vanishing of $L(\mathcal{E}_q, s)$ at $s = 1$ equals the categorical rank:

$$
\mathrm{ord}_{s=1} L(\mathcal{E}_q, s) = r_q.
$$

**(Full $q$-BSD).**
The leading Taylor coefficient satisfies

$$
\frac{L^{(r_q)}(\mathcal{E}_q, 1)}{[r_q]_q!} = \frac{\Omega_q \cdot \mathrm{Reg}_q(\mathcal{E}_q) \cdot |\mathrm{Sha}_q(\mathcal{E}_q)| \cdot \displaystyle\prod_{\mathfrak{m}} c_{\mathfrak{m}}(q)}{|\mathcal{E}_q(\mathbf{1})_{\mathrm{tors}}|^2_q},
$$

where $[r_q]_q! = [1]_q \cdot [2]_q \cdots [r_q]_q$ is the $q$-factorial, $\Omega_q$ is the Reeb period, $\mathrm{Reg}_q$ is the $q$-regulator (determinant of the $q$-Neron--Tate height pairing), and $c_\mathfrak{m}(q)$ are the Tamagawa numbers.

When $r_q = 0$, the regulator is $\mathrm{Reg}_q = 1$ (determinant of the empty matrix), the torsion subgroup is trivial, and the formula collapses to

$$
L(\mathcal{E}_q, 1) = \Omega_q \cdot |\mathrm{Sha}_q(\mathcal{E}_q)| \cdot \prod_{\mathfrak{m}} c_{\mathfrak{m}}(q).
$$
