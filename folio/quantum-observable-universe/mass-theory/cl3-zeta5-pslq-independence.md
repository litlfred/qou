*PSLQ searches at 70 decimal places with a coefficient norm bound of $10^8$ certify that the difference*

$$
  X \;:=\; \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right) - \mathrm{Cl}_3\!\left(\tfrac{4\pi}{5}\right)
  \;\approx\; 0.955723\ldots
$$

*admits no $\mathbb{Q}$-linear relation with any standard weight-3 period basis elements.*

The test subjects $X$ against candidate bases including $\{\zeta(3), \pi^3\}$ and full golden-ratio logarithmic bases. No relation emerges. While not a proof of irreducibility, the negative PSLQ result provides the strongest unconditional canonical evidence that $X$ constitutes a genuinely independent depth-3 period. The depth-3 surface for $\mathbb{Q}(\zeta_5)$ reduces to this single real period.

What is proved is the identification of $X$: the coefficient $\cos(2\pi n/5) - \cos(4\pi n/5)$ equals $\tfrac{\sqrt5}{2}\,\chi_5(n)$, where $\chi_5$ is the quadratic character modulo 5, so

$$
  X \;=\; \tfrac{\sqrt5}{2}\, L(3, \chi_5),
  \qquad L(3, \chi_5) \;=\; \sum_{n \geq 1} \frac{\chi_5(n)}{n^3}.
$$

The $\mathbb{Q}$-linear independence of $L(3,\chi_5)$ from $\zeta(3)$ and $\pi^3$ is not known; the PSLQ result is evidence for it, not a proof.

Comparison with the standard-relation dimension bound for $\mathrm{MPV}(3,5)$ clarifies the scope of the candidate basis. At weight $3$ and prime level $N = 5$, the $5^2(5+1) = 150$ multiple polylogarithm values satisfy Deligne and Goncharov's motivic upper bound $d(3,5) \le D(3,5) = (\varphi(5)/2 + 1)^3 = 27$, which finite and regularized double-shuffle relations together with lifted weight-$1$ relations tighten to $d(3,5) \le \mathrm{SR}(3,5) = 22 = (5^3 + 4\cdot 5^2 + 5\cdot 5 + 14)/12$ \cite[\S\S 7.3--7.4, \S 9 Table~2, Conj.~9.2]{zhao2010-standard-relations}. Of the eight periods tested against $X = \tfrac{\sqrt{5}}{2} L(3,\chi_5) \in \mathrm{Re}\,\mathrm{MPV}(3,5)$, the five level-$1$ and level-$5$ terms $\{\zeta(3), \pi^3, \pi\log^2\varphi, \log^3\varphi, \pi^2\log\varphi\}$ span the real level-$1$ line and decomposable lower-weight products inside $\mathrm{MPV}(3,5)$, while $\{\pi\log^2 2, \pi^2\log 2, \log^3 2\}$ test cross-level independence against level $2$; the remaining dimension up to $\mathrm{SR}(3,5) = 22$ accommodates $X$ alongside imaginary parity components and higher-depth generators $L_5(2,1\mid \cdot)$ and $L_5(1^3\mid \cdot)$.
