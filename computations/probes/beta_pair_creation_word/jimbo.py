"""Jimbo Ř representation of H_N(q) on V^{⊗N}, V = span(u, d), exact.

Basis vectors are tuples of 0 (u, T³ = +½, K u = q u) and 1 (d). Ř on positions (i, i+1), columns
are images (as ChargedCurrentW.Rc, branch claude/qbeta-n1-charged-w-element-2026-11-20):
uu ↦ q uu, ud ↦ du, du ↦ ud + h du, dd ↦ q dd. Ř² = hŘ + 1, so σ_i ↦ Ř_i is a representation.
ρ(xy) = ρ(x)ρ(y) acting on column vectors: a word is applied right to left.
"""
from __future__ import annotations

from hecke_exact import RING, ZERO, ONE, h, q, H, reduced_word

QR = RING(q)
HR = RING(h)


def apply_gen(vec, i, inv=False):
    out: dict = {}
    for b, c in vec.items():
        a, bb = b[i], b[i + 1]
        if a == bb:
            terms = [(b, QR)]
        elif (a, bb) == (0, 1):
            sw = list(b); sw[i], sw[i + 1] = 1, 0
            terms = [(tuple(sw), ONE)]
        else:  # du -> ud + h du
            sw = list(b); sw[i], sw[i + 1] = 0, 1
            terms = [(tuple(sw), ONE), (b, HR)]
        for bv, cv in terms:
            out[bv] = out.get(bv, ZERO) + c * cv
        if inv:  # Ř⁻¹ = Ř − h
            out[b] = out.get(b, ZERO) - c * HR
    return {k: v for k, v in out.items() if v != 0}


def apply_word(vec, word):
    for g in reversed(word):
        vec = apply_gen(vec, g, inv=False) if g >= 0 else apply_gen(vec, -g - 1, inv=True)
    return vec


def apply_H(vec, X: H):
    out: dict = {}
    for w, c in X.c.items():
        img = apply_word(vec, reduced_word(w))
        for k, v in img.items():
            out[k] = out.get(k, ZERO) + v * c
    return {k: v for k, v in out.items() if v != 0}
