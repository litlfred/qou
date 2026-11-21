import { prose } from "../../schema/builders";

export default prose({ label: "sec:molecular-chains-rings-intro",
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): A **[molecular Hopf chain](#def:molecular-hopf-chain)** of length $N$ composes $N - 1$ covalent bonds along a backbone, giving a tridiagonal linking matrix with free endpoint sites. To pass to closed rings, replace the naïve picture — $N$ pairwise Hopf links — with a single non-local invariant: the **[threading link](#def:threading-link)** $T(2,N)$. Its braid word winds twice through every atom, and its reduced Alexander polynomial at $t = 1$, the linking number $N/2$, is half the pairwise linking number $N$. A **[molecular Hopf ring](#def:molecular-hopf-ring)** binds atoms globally by the threading link rather than locally by Hopf links." },
  ] });
