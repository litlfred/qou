*Combining the Wenzl-bridge closed form for $y_\lambda(q)$ with the q-Murnaghan-Nakayama rule for $\chi_\lambda(T_w; q)$ evaluates the Markov trace exactly:*

$$
  \mathrm{tr}_M(T_w) \;=\; \sum_{\lambda \,\vdash\, n} y_\lambda(q) \cdot \chi_\lambda(T_w; q).
$$

*The combined algorithm runs in $O(p(n) \cdot (\max\text{hooks} + n^2))$ time. This bypasses the $O(p(n) \cdot \dim_\lambda^2 \cdot \ell(w))$ Hoefsmit-seminormal bottleneck.*

This synergy drops mass-formula calculation times from hours to seconds for large $n$. The identity $\mathrm{tr}_M(T_w) = z^{\ell(w)}$ is **not** a valid cross-check in general. It holds when the reduced word of $w$ uses each generator at most once: the largest generator then occurs once, cyclicity moves it to the end, and the Markov property removes it with a factor $z$. It fails as soon as a generator repeats. For $w = s_1 s_2 s_1$ under convention D, $\mathrm{tr}_M(T_w) = hz^2 + z = q^{3}(q^{4}+1)/(q^{2}+1)^{2}$, while $z^{3} = q^{9}/(q^{2}+1)^{3}$; at $q = 2$ these are $136/25$ and $512/125$ ([corrected Markov trace](#prop:corrected-markov-trace)).
