**Statement.**
The benzene aromatic stabilisation energy (Kekulé reference) is, at
leading order in the Alexander-weight encoding,

$$
  E_{\mathrm{res}}(\mathrm{benzene})
   = 
  \bigl[\,3 - \Delta_{T(2,6)}(q_{0})\,\bigr]\,
  \lvert q + q^{-1}\rvert_{\mathrm{mol}},
$$

where $3$ is the count of localised C=C double bonds in the Kekulé
structure (each contributing one Hopf-link weight) and
$\Delta_{T(2,6)}(q_{0})$ is the threading-link Alexander weight at
the substrate value.

**Classical limit.**
By [$\Delta_{T(2,N)}$ closed form](#lem:alexander-T2N-closed-form),
$\Delta_{T(2,6)}(1) = 3$ exactly, so the residual vanishes in the
classical limit:

$$
  \lim_{q \to 1}\, E_{\mathrm{res}}(\mathrm{benzene}) = 0.
$$

This means the *single-link* Alexander-weight residual is **not** the
source of the experimental aromatic stabilisation
($\sim 150\ \mathrm{kJ/mol}$).  Instead, the resonance arises from the
*coherent delocalisation* encoded in the threading link as a whole
(see [threading half-weight](#prop:threading-half-weight)) plus the
bond-order energy refinement in [bond-order energy
formula](#prop:bond-order-energy-formula).

**Proof.**
By [ring closure barrier (quantitative)](#prop:ring-closure-barrier-quantitative)
specialised at $N = 6$, the ring-closure energy gain is
$\bigl[(N-1) - \Delta_{T(2,6)}(q_{0})\bigr]\cdot\lvert q+q^{-1}\rvert_{\mathrm{mol}}$,
which subtracts the chain weight from the threading weight.  The
*resonance* energy is the analogous expression with the Kekulé
reference $3$ in place of the chain weight $5$, hence
$\bigl[3 - \Delta_{T(2,6)}(q_{0})\bigr]\cdot\lvert q+q^{-1}\rvert_{\mathrm{mol}}$.
$\square$

**Caveat.**
At the substrate value $q_{0} \approx 1.11$,
$\Delta_{T(2,6)}(q_{0}) \approx 3.04 > 3$, so the predicted resonance
is small and *negative* — opposite in sign to the experimental
aromatic stabilisation.  The chapter resolves this by including
higher-order Alexander corrections and the bond-order term; the
present corollary captures only the leading topological contribution.
