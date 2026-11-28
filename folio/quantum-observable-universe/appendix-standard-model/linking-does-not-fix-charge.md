**Proposition.** Over the three-strand words of the corpus, with linking sum
$\mathrm{linkSum} = 2\,\mathrm{lk}$ as in `RingMassLinkingThreeStrand`:

1. the leptons $e = \sigma_1\sigma_2\sigma_1$, $\mu = \sigma_1^2\sigma_2^{-1}$,
   $\tau = \sigma_1^4\sigma_2^{-1}$ have linking sums $2, 2, 4$ and all carry charge $-1$;
2. the proton $(\sigma_1\sigma_2^{-1})^3$ and the neutral $4_1 = (\sigma_1\sigma_2^{-1})^2$ both
   have linking sum $0$, with charges $+1$ and $0$, so electric charge is not a function of
   the linking sum;
3. mirroring the electron word negates its linking sum and leaves its strand permutation
   unchanged.

So the linking sign is the handedness of the braid, a parity-type datum, while the open
sign of [`prop:chirality-sign-is-hypercharge-sign`](chirality-sign-is-hypercharge-sign.md)
is a charge-conjugation-type datum ($Y \mapsto -Y$). The linking number, alone, does not fix
it.

**Proof.** Finite computation on the words.

**Scope.** This is a negative for linking alone. It does not exclude a rule that combines a
word's linking with its strand subset.

## Lean structure

`QOU.EightfoldWay.LinkingDoesNotFixCharge`: `lepton_linkSums`, `proton_higgs_linkSum`,
`charge_not_function_of_linkSum`, `mirror_negates_linkSum`. Sorry-free.
