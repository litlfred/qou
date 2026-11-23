**Proposition (conditional on [Quarks as Borromean-linked unknots in the exceptional divisor](#conj:borromean-quark)).**
Let $e^- = \sigma_0\sigma_1\sigma_0 \in B_3$ be the electron word ([electron knot](#def:electron-knot)), whose closure is the Hopf link, Hopf-linked to a proton anchor. For $n \geq 1$ let the level-$n$ word be

$$
  e_n = \sigma_0\sigma_1\sigma_0\,\sigma_2\sigma_3\cdots\sigma_n \in B_{n+2},
  \qquad e_1 = e^-,
$$

obtained from $e^-$ by $n - 1$ strand-adding curls. Let $w$ be the writhe (exponent sum) of $e_n$.

1. **Shell--writhe correspondence.** Each curl appends the next generator, which is a Markov stabilisation, so the closure of $e_n$ is still the Hopf link. The writhe of $e_n$ is $w = n + 2$, so the level is $n = w - 2$. The ground state has $w = 3$ ($n = 1$).
2. **Orbital counting.** Not re-derived for the ruled electron. The count $\sum_{\ell=0}^{n-1}(2\ell + 1) = n^2$ was built on the resonance modes of a trefoil in its normal bundle (the backup reading below). The closure of $e_n$ has two components, and no counterpart of that normal-bundle construction is on record for it.
3. **Energy scaling.** Not re-derived for the ruled electron. The scaling $E_n = -E_{\mathrm{ion}}/n^2$ rested on the Seifert-surface-area argument of the backup reading.

Item 1 is proved in Lean (`writhe_levelWord` and `shell_eq_writhe_sub_two` in `QOU.BraidKnot.ElectronLevelWord`); Markov's theorem, which keeps the closure the Hopf link, is quoted rather than formalised.

**Backup reading.** If the electron is the trefoil $\sigma_0^{2n+1} \in B_2$, the level is $n = (w - 1)/2$ with $w = 2n + 1$. The two readings agree at the ground state $w = 3$, $n = 1$ and differ from $n = 2$ on.

**Archimedean specialisation.** What follows evaluates generic $q$-deformation identities at the real-valued substrate parameter $q_0$. The categorical identities remain valid over any abstract coefficient ring.
