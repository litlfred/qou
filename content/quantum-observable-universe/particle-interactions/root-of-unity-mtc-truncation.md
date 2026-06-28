**Conjecture (root-of-unity MTC truncation).**
*Let $H_n(R, q)$ be the Iwahori–Hecke algebra of the
[anyonic substrate](#conj:hecke-anyonic-substrate), and fix
$k \geq 2$.  Specialise the deformation parameter at a primitive
$k$-th root of unity on the unit circle,*

$$
  q \;=\; e^{2\pi i / k} \;\in\; S^1.
$$

*Then the cyclotomic quotient of the corresponding KLR algebra
realising $H_n(R, q)$ becomes finite-dimensional, the infinite
Kashiwara crystal $\mathrm{Cryst}(\mathfrak{sl}_n)$ truncates to a
finite component supported on partitions with at most $k - 1$
columns, and the resulting category of cyclotomic-KLR modules is a
Modular Tensor Category $\mathrm{MTC}_k$ \cite{bakalovkirillov2001}.
The simple objects of $\mathrm{MTC}_k$ are non-abelian anyons
\cite{kitaev2006, nayak2008}: their fusion rules are determined by
the truncated crystal's Littlewood–Richardson coefficients, and their
braiding is the action of $B_n$ on $H_n(R, q)$ specialised at $q =
e^{2\pi i / k}$.*

**Algorithmic role.**
*Switching the substrate parameter from generic to a primitive
$k$-th root of unity converts the open-ended Hecke evaluation into a
finite-rank fusion calculation: the engine enumerates the truncated
crystal nodes and reads off the $F$- and $R$-matrices of
$\mathrm{MTC}_k$ directly from the $\sigma_{s_i}$ generators evaluated at
the chosen root.*

**Conjectural status.**
*The Bakalov–Kirillov MTC structure on cyclotomic-KLR modules at a
root of unity is established \cite{bakalovkirillov2001,
khovanovlauda2009}, as is the truncation of the Kashiwara crystal at
roots of unity \cite{kashiwara1991}.  What remains conjectural is the
identification of the simple $\mathrm{MTC}_k$ objects with the QOU
substrate's non-abelian anyon spectrum at the chosen $k$, including
the precise correspondence between QOU particle labels and crystal-
truncated highest-weight vectors.  Falsification is by exhibiting a
QOU particle at $q = e^{2\pi i / k}$ whose fusion does not match the
predicted $\mathrm{MTC}_k$ rule.*
