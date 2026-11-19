import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wigner-np-pairing",
  authorNotes: [
    { kind: "caveat", date: "2026-10-11", body: "The value $m_e[3]_q[2]_q^2$ is **stated, not derived**. The Lean reference `wigner_energy_from_22` is the commutativity identity `w*v*α*Z = α*w*Z*v` (`ring`), which says nothing about $[3]_q[2]_q^2$, and `uses` is empty. The same number is the shell coefficient $\\delta_S = [2]_q^2[3]_q m_e$, and `derived-mass-formula-light-isotopes` pairs it with $\\min(Z,N)/A$ rather than $T(T+1)/A$. Agreement with an empirical Wigner value is not evidence under the no-fitting rule. Two inconsistent definitions of $C_\\lambda$ (bean `qou-wg3c`). `prf:unified-iterative-correction` states $C_\\lambda = m_e\\,H_q(\\lambda)$ (the $q$-hook product), while `prop:mass-coefficient-shadow-price` carries $C_\\lambda = w_\\lambda\\,h/2$ as the class field `C_eq`. " +
      /* <!-- literal-source: closed-form q-hook evaluation m_e * H_q((2,2)) = m_e * [3]_q * [2]_q^2 = 6.2893 MeV at q_0 --> */
      "At $(2,2)$ these give $6.2893$ MeV and $m_e w h/2 = 0.00887$ MeV; no stated map relates them. Neither is derived: the hook value is asserted universal and fails for six of the seven mass-formula coefficients (`qou-orjl`), and the factorisation $u^*_\\lambda = C_\\lambda S_\\lambda(Z,N,A)$ is a class field the stated LP cannot produce, since its dual constraints carry no $(Z,N)$." },
  ],
  title:
    "Wigner energy from $T{=}0$ np pairing: $(2,2)$ partition at $k{=}4$",
  lean: { ref: "qou:QOU.Archimedean.ConfinedKnotBinding.wigner_energy_from_22",
    validation: "not_checked",
  },
  uses: [],
  computation: {
    engine: "python",
    script: "computations/b_over_a_evaluator.py",
    witness: [
      "computations/b-over-a.witness.json",
      "computations/probes/casimir-q-zeta-probe.witness.json",
    ],
    status: "verified",
    requires: ["mpmath"],
  },
  cites: [
    "kerov1996",
    "feray-meliot2012",
    "satula1997",
  ],
  tags: [
    "wigner-energy",
    "np-pairing",
    "partition-22",
    "binding",
    "q-hook-product",
  ],
});
