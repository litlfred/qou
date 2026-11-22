**Proposition.** Let $K$ be a field, $q \in K$ with $q \neq 0$ and $q^2 + 1 \neq 0$, and let $\check R$ be Jimbo's braiding of $U_q(\mathfrak{gl}_3)$ on $(K^3)^{\otimes n}$. Let $b$ be a flavour Hecke generator, $(b - q)(b + q^{-1}) = 0$, and let $X = \check R_{\mathrm{colour}} \cdot b$ be the tensor braiding of a strand carrying colour and flavour.

1. $\check R$ satisfies the Hecke relation and the braid relation, and commutes with the coproducts of $E_i$, $F_i$ and $L_j$.
2. The colour singlets in $(K^3)^{\otimes 3}$ form the line spanned by the $q$-antisymmetric vector $\varepsilon_q$, and each braid generator acts on $\varepsilon_q$ as $-q^{-1}$.
3. On the colour-singlet sector $X = -q^{-1} b$, and the rescaled generator satisfies $-q X = b$.
4. For a braid word $w$ with exponent sum $e(w)$ and any linear trace $\tau$, the value of $\tau$ on $w$ evaluated in the generators $X$ is $(-q^{-1})^{e(w)}$ times its value in the generators $b$. Evaluated in the rescaled generators $-qX$, every value equals its flavour value.

**Proof.** Items 1 and 2 are `hecke`, `braid`, `comm_E`, `comm_F`, `comm_L`, `R12_eps`, `R23_eps`, `E_eps`, `F_eps`, `L_eps` and `singlet_unique` in `QOU.Braiding.JimboGl3Singlet`. Item 3 is `singlet_hecke` and `singlet_rescale` in `QOU.Braiding.HopfColourTensorBraid`. Item 4 is `word_eval_smul` and `trace_word_smul` in `QOU.Braiding.ColourSingletDownstream`, applied to the central scalar $c = -q^{-1}$ and, for the rescaled generators, to $c = 1$. All are sorry-free. $\square$

On the raw generators the per-bond factor $-q^{-1} z_D = -q^2/(q^2+1)$ is negative for real $q > 0$ (`raw_pp_factor`), so a bond law of the form $\log(1/f)$ is stated in the rescaled generators $b = -qX$. With that choice every Markov trace value of a hadron word on the colour-singlet sector, and every per-bond factor, is the flavour value.

The gl₆ coideal route gives the singlet generator $-b^{-1}$, the image of $b$ under the Hecke involution $\sigma \mapsto -\sigma^{-1}$; it satisfies $(-b^{-1})(-q^{-1} b) = q^{-1}$ (`coideal_mul_tensor`), so the two routes agree on the singlet sector up to that involution.
