#!/usr/bin/env python3
"""Does pp = nn survive when the core braids strands of the two nucleons? (exact, generic q)

PRE-REGISTRATION (written before the first run, audit §35).
Question: §34 proves pp = nn for the two-nucleon q-Casimir readout when the core sits inside the
blocks. Here the core also contains crossings between strand 2 (block A) and strand 3 (block B).
Readout and pair operator are exactly those of np_gaudin_generic_q_probe.py.
Decision rule, per core: report d = TX[pp]*T1[nn] - TX[nn]*T1[pp] in Z[q, q^-1].
  d == 0 for every core  -> pp = nn extends to cross-nucleon cores (Lean next).
  d != 0 for some core   -> the in-block restriction of §34 is load-bearing; record which cores break
                            it and the sign of the split at q > 1. No fitting, no tuning of the cores:
                            the list below is fixed in advance.
Cores (fixed list): base = the §28 in-block core (σ0σ1⁻¹ alternating in each block), times
  (a) σ2, (b) σ2⁻¹, (c) σ2², (d) σ2σ3σ1σ2 (two strands swap blocks), (e) the full twist β_AB² (control:
  claim 3 of the generic-q probe, expected d = 0).
"""
import np_gaudin_generic_q_probe as GQ

P, LP, q = GQ.P, GQ.LP, GQ.q


def main():
    S = P.setup(q)
    S = {k: ([[LP.of(x) for x in r] for r in v] if isinstance(v, list) else v) for k, v in S.items()}
    A, B, AB = [0, 1, 2], [3, 4, 5], list(range(6))
    V = [(0, False), (1, True)] * 3 + [(3, False), (4, True)] * 3
    Kd = {s: q ** (2 * sum(1 for x in P.bits(s) if x == 0) - P.N) for s in range(P.D)}
    X = P.add(GQ.scaled_casimir(S, AB), GQ.scaled_casimir(S, A), GQ.scaled_casimir(S, B), coeffs=[1, -1, -1])
    full = [(2, False), (1, False), (0, False), (3, False), (2, False), (1, False), (4, False), (3, False), (2, False)]
    cores = {
        "(a) base*s2": V + [(2, False)],
        "(b) base*s2^-1": V + [(2, True)],
        "(c) base*s2^2": V + [(2, False), (2, False)],
        "(d) base*s2 s3 s1 s2": V + [(2, False), (3, False), (1, False), (2, False)],
        "(e) base*beta_AB^2 (control)": V + full + full,
    }
    pp, nn = (1, 1), (0, 0)
    for name, word in cores.items():
        base = P.word(S, word)
        T1 = P.readout(S, base, Kd, P.eye())
        TX = P.readout(S, base, Kd, X)
        d = TX.get(pp, LP()) * T1.get(nn, LP()) - TX.get(nn, LP()) * T1.get(pp, LP())
        print(f"{name}: pp = nn identically in q: {d == 0}")
        if d != 0:
            print(f"   d = {d}")
            print(f"   T1[pp] = {T1.get(pp)}\n   T1[nn] = {T1.get(nn)}")


if __name__ == "__main__":
    main()
