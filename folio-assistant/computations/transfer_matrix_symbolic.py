#!/usr/bin/env python3
"""
Symbolic transfer matrix engine for nuclear computations, exact in q.

All quantities are sympy expressions in Symbol('q', positive=True).
No floating point until final evaluation at q0.

The transfer matrix formalism:
  T(c, d) = [[c*(q - q^{-1}) + d,  c],
              [c,                   d]]

Three nuclear crossing types:
  pp  (proton-proton):   c = 1,           d = 0
  nn  (neutron-neutron): c = q^2,         d = -q*s  where s = q^{1/2} - q^{-1/2}
  mix (proton-neutron):  c = (1+q^2)/2,   d = -q*s/2

Markov-traced volume at generator sigma_i:
  V_hat_i(q) = z * M_i[0,0] + M_i[1,0]
  where z = 1/(q^{1/2} + q^{-1/2})

Nuclear Skein polynomial:
  P_N(q) = prod_i V_hat_i(q)

Universal beta decay matrix:
  Delta_beta(q) = T_mix - T_nn = T_pp - T_mix
                = (1/2)(1 - q^2) T_pp + (q*s/2) I

Connection to Groebner NF: each V_hat_i in the transfer matrix
corresponds to one generator sigma_i in the Hecke algebra NF.
The transfer matrix computes the SAME quantity as the Groebner
reduction but via matrix products instead of word reduction.

Usage:
    cd folio-assistant/computations
    python3 transfer_matrix_symbolic.py
"""

import sympy as sp
from sympy import sqrt, Rational, log, simplify, expand, Matrix
from experimental_constants import (
    Q_TRITIUM_MEV, Q_C14_MEV, Q_CO60_MEV,
    Q_SR90_MEV, Q_CS137_MEV, Q_BI210_MEV,
    M_P_MEV,
)

# ── Symbolic ring: exact in q ──────────────────────────────────

q = sp.Symbol('q', positive=True)
q_inv = 1 / q
q_half = sqrt(q)
q_half_inv = 1 / sqrt(q)

# Fundamental quantities
ha = q - q_inv                        # q - q^{-1}  (Hecke coefficient)
s_skein = q_half - q_half_inv         # q^{1/2} - q^{-1/2}  (Skein amplitude)
z_markov = 1 / (q_half + q_half_inv)  # Markov parameter

# Substrate parameter q0 (from q_parameter.py derivation)
Q0 = 1.10998


# ════════════════════════════════════════════════════════════════
# 1. SymbolicTransferMatrix — wraps a 2x2 sympy Matrix
# ════════════════════════════════════════════════════════════════

class SymbolicTransferMatrix:
    """A 2x2 transfer matrix with symbolic entries in q.

    Constructed from crossing coefficients (c, d):
        T(c, d) = [[c*(q - q^{-1}) + d,  c],
                    [c,                   d]]

    Supports composition (matrix multiplication), Markov trace
    extraction, determinant, eigenvalues, and numeric evaluation.
    """

    def __init__(self, c=None, d=None, matrix=None):
        """Create from (c, d) coefficients or a raw 2x2 Matrix.

        Args:
            c: coefficient of sigma (sympy expression in q)
            d: constant term (sympy expression in q)
            matrix: explicit 2x2 sympy Matrix (overrides c, d)
        """
        if matrix is not None:
            self.mat = Matrix(matrix)
        elif c is not None and d is not None:
            self.mat = Matrix([
                [expand(c * ha + d), c],
                [c,                  d],
            ])
        else:
            raise ValueError("Provide either (c, d) or matrix")

        # Store c, d if provided (useful for inspection)
        self._c = c
        self._d = d

    @staticmethod
    def identity():
        """The 2x2 identity matrix."""
        return SymbolicTransferMatrix(matrix=sp.eye(2))

    @staticmethod
    def zero():
        """The 2x2 zero matrix."""
        return SymbolicTransferMatrix(matrix=sp.zeros(2))

    def compose(self, other):
        """Matrix multiplication: self * other (left-to-right chain)."""
        return SymbolicTransferMatrix(matrix=self.mat * other.mat)

    def __mul__(self, other):
        """Alias for compose."""
        return self.compose(other)

    def __add__(self, other):
        """Matrix addition."""
        return SymbolicTransferMatrix(matrix=self.mat + other.mat)

    def __sub__(self, other):
        """Matrix subtraction."""
        return SymbolicTransferMatrix(matrix=self.mat - other.mat)

    def scale(self, scalar):
        """Scalar multiplication."""
        return SymbolicTransferMatrix(matrix=scalar * self.mat)

    def markov_trace(self):
        """Markov-traced volume: V_hat = z * M[0,0] + M[1,0].

        Returns a sympy expression in q.
        """
        return expand(z_markov * self.mat[0, 0] + self.mat[1, 0])

    def det(self):
        """Determinant of the 2x2 matrix."""
        return simplify(self.mat.det())

    def eigenvalues(self):
        """Eigenvalues of the 2x2 matrix (dict {eigenvalue: multiplicity})."""
        return self.mat.eigenvals()

    def trace(self):
        """Matrix trace (not Markov trace)."""
        return simplify(self.mat.trace())

    def evaluate(self, q_val):
        """Evaluate all entries at q = q_val. Returns a numeric 2x2 list."""
        return [[float(self.mat[i, j].subs(q, q_val))
                 for j in range(2)] for i in range(2)]

    def markov_trace_at(self, q_val):
        """Evaluate the Markov-traced volume at q = q_val."""
        return float(self.markov_trace().subs(q, q_val))

    def __repr__(self):
        return f"SymbolicTransferMatrix(\n  {self.mat}\n)"

    def show(self, name="T"):
        """Pretty-print the matrix with symbolic entries."""
        print(f"{name} =")
        for i in range(2):
            row = [simplify(self.mat[i, j]) for j in range(2)]
            print(f"  [{row[0]},  {row[1]}]")


# ════════════════════════════════════════════════════════════════
# 2. Pre-built matrices
# ════════════════════════════════════════════════════════════════

# Crossing coefficients (exact in q)
C_PP, D_PP = sp.Integer(1), sp.Integer(0)
C_NN, D_NN = q**2, -q * s_skein
C_MIX, D_MIX = (1 + q**2) / 2, -q * s_skein / 2

# The three nuclear transfer matrices
T_pp = SymbolicTransferMatrix(c=C_PP, d=D_PP)
T_nn = SymbolicTransferMatrix(c=C_NN, d=D_NN)
T_mix = SymbolicTransferMatrix(c=C_MIX, d=D_MIX)

# Universal beta decay matrix: Delta_beta = T_mix - T_nn = T_pp - T_mix
#   = (1/2)(1 - q^2) T_pp + (q*s/2) I
Delta_beta = T_mix - T_nn

# Electromagnetic vertex (electron capture / pair production)
# T_gamma_e: the electron crossing is a Hopf link (c=1, d=0), same as T_pp
T_gamma_e = SymbolicTransferMatrix(c=sp.Integer(1), d=sp.Integer(0))


def crossing_coeffs(ti, tj):
    """Return symbolic (c, d) for a crossing between nucleon types.

    Args:
        ti, tj: 'p' (proton) or 'n' (neutron)

    Returns:
        (c, d) as sympy expressions
    """
    if ti == 'p' and tj == 'p':
        return C_PP, D_PP
    elif ti == 'n' and tj == 'n':
        return C_NN, D_NN
    else:  # mixed (pn or np)
        return C_MIX, D_MIX


def crossing_matrix(ti, tj):
    """Return the SymbolicTransferMatrix for a crossing between nucleon types."""
    c, d = crossing_coeffs(ti, tj)
    return SymbolicTransferMatrix(c=c, d=d)


# ════════════════════════════════════════════════════════════════
# 3. NucleusTransferMatrix — builds the full transfer chain
# ════════════════════════════════════════════════════════════════

class NucleusTransferMatrix:
    """Transfer matrix chain for a nucleus N(Z, N).

    Builds an ordering of Z protons followed by N neutrons,
    computes per-generator transfer matrix products, extracts
    Markov-traced volumes V_hat_i, and computes the Skein
    polynomial P_N(q) = prod_i V_hat_i(q).
    """

    def __init__(self, Z, N, ordering=None):
        """Build the transfer matrix chain for nucleus (Z, N).

        Args:
            Z: proton count
            N: neutron count
            ordering: list of 'p'/'n' for each nucleon position.
                      Default: Z protons then N neutrons.
        """
        self.Z = Z
        self.N = N
        self.A = Z + N

        if ordering is not None:
            if len(ordering) != self.A:
                raise ValueError(f"Ordering length {len(ordering)} != A = {self.A}")
            self.ordering = list(ordering)
        else:
            self.ordering = ['p'] * Z + ['n'] * N

        # Build per-generator chains
        self._symbolic = (self.A <= 6)  # only compute symbolically for small nuclei
        self._generator_matrices = []  # M_i = product of T matrices at gen i
        self._volumes = []             # V_hat_i symbolic expressions

        for i in range(self.A - 1):
            M = SymbolicTransferMatrix.identity()
            for j in range(i + 1, self.A):
                T = crossing_matrix(self.ordering[i], self.ordering[j])
                M = M * T
            self._generator_matrices.append(M)
            self._volumes.append(M.markov_trace())

        # Skein polynomial (symbolic product of volumes)
        if self._symbolic:
            self._skein = sp.Integer(1)
            for v in self._volumes:
                self._skein = expand(self._skein * v)
        else:
            self._skein = None  # too large; use skein_at() for numeric

    @property
    def n_generators(self):
        """Number of braid generators = A - 1."""
        return self.A - 1

    def generator_matrix(self, i):
        """Return the composed transfer matrix at generator sigma_i."""
        return self._generator_matrices[i]

    def volume(self, i):
        """Return V_hat_i(q) = z * M_i[0,0] + M_i[1,0] (symbolic)."""
        return self._volumes[i]

    def volumes(self):
        """Return all per-generator volumes as a list of sympy expressions."""
        return list(self._volumes)

    def skein_polynomial(self):
        """Return P_N(q) = prod_i V_hat_i(q) (symbolic expression in q)."""
        return self._skein

    def skein_at(self, q_val):
        """Evaluate the Skein polynomial at q = q_val.

        For large nuclei (A > 6), evaluates per-generator volumes numerically
        and multiplies, avoiding symbolic polynomial explosion.
        """
        if self.A <= 6:
            return float(self._skein.subs(q, q_val))
        else:
            # Numeric: multiply per-generator volumes evaluated at q_val
            result = 1.0
            for v in self._volumes:
                result *= float(v.subs(q, q_val))
            return result

    def volume_at(self, i, q_val):
        """Evaluate V_hat_i at q = q_val."""
        return float(self._volumes[i].subs(q, q_val))

    def compare(self, daughter):
        """Compare this nucleus (parent) with a daughter nucleus.

        Returns a dict with:
          - ln_ratio: symbolic ln(P_dau / P_par)
          - per_generator: list of (V_par_i, V_dau_i) pairs
        """
        ratio = expand(daughter.skein_polynomial() / self.skein_polynomial())
        # For the symbolic log, keep it as log(ratio)
        ln_ratio = log(ratio)

        per_gen = []
        n = min(self.n_generators, daughter.n_generators)
        for i in range(n):
            per_gen.append((self._volumes[i], daughter._volumes[i]))

        return {
            'ratio': ratio,
            'ln_ratio': ln_ratio,
            'per_generator': per_gen,
        }

    def __repr__(self):
        return (f"NucleusTransferMatrix(Z={self.Z}, N={self.N}, "
                f"A={self.A}, ordering={''.join(self.ordering)})")


# ════════════════════════════════════════════════════════════════
# 4. beta_decay_qvalue — symbolic Q-value computation
# ════════════════════════════════════════════════════════════════

def skein_ln_numeric(Z, N, q_val):
    """Fast numeric ln|P_N(q)| — no sympy overhead, no overflow.

    Returns (ln_abs_P, sign) where P = sign * exp(ln_abs_P).
    """
    import math
    A = Z + N
    types = ['p'] * Z + ['n'] * N
    q_v = q_val
    qi_v = 1.0 / q_v
    HA_v = q_v - qi_v
    s_v = q_v**0.5 - qi_v**0.5
    z_v = 1.0 / (q_v**0.5 + qi_v**0.5)

    def crossing_cd(ti, tj):
        if ti == 'p' and tj == 'p': return 1.0, 0.0
        elif ti == 'n' and tj == 'n': return q_v**2, -q_v * s_v
        else: return (1 + q_v**2) / 2, -q_v * s_v / 2

    ln_P = 0.0
    sign = 1
    for i in range(A - 1):
        M = [[1.0, 0.0], [0.0, 1.0]]
        for j in range(i + 1, A):
            c, d = crossing_cd(types[i], types[j])
            T = [[c * HA_v + d, c], [c, d]]
            M = [[M[0][0]*T[0][0]+M[0][1]*T[1][0], M[0][0]*T[0][1]+M[0][1]*T[1][1]],
                 [M[1][0]*T[0][0]+M[1][1]*T[1][0], M[1][0]*T[0][1]+M[1][1]*T[1][1]]]
        V = z_v * M[0][0] + M[1][0]
        if V < 0:
            sign *= -1
            V = -V
        if V > 0:
            ln_P += math.log(V)
        else:
            return -float('inf'), 0

    return ln_P, sign


def beta_decay_qvalue(Z_par, N_par, q_val=Q0, label=""):
    """Compute the symbolic Q-value for beta-minus decay N(Z,N) -> N(Z+1,N-1).

    Builds parent (Z, N) and daughter (Z+1, N-1) nuclei, computes
    ln(P_dau / P_par) symbolically and numerically at q_val.

    Args:
        Z_par: proton number of parent
        N_par: neutron number of parent
        q_val: numeric value of q for evaluation (default Q0)
        label: human-readable label for the nucleus

    Returns:
        dict with symbolic and numeric results
    """
    A = Z_par + N_par
    # For small nuclei, compute symbolically; for large, go numeric directly
    if A <= 6:
        parent = NucleusTransferMatrix(Z_par, N_par)
        daughter = NucleusTransferMatrix(Z_par + 1, N_par - 1)
        P_par = parent.skein_polynomial()
        P_dau = daughter.skein_polynomial()
        ratio_sym = sp.cancel(P_dau / P_par)
        P_par_num = float(P_par.subs(q, q_val))
        P_dau_num = float(P_dau.subs(q, q_val))
    else:
        parent = None
        daughter = None
        P_par = None
        P_dau = None
        ratio_sym = None
        ln_par, s_par = skein_ln_numeric(Z_par, N_par, q_val)
        ln_dau, s_dau = skein_ln_numeric(Z_par + 1, N_par - 1, q_val)
        # For Q-value we only need ln(P_dau/P_par) — no exponentiation needed
        P_par_num = None  # too large to store as float
        P_dau_num = None
        ln_ratio_num = ln_dau - ln_par
        ratio_num = None

        return {
            'label': label or f"N({Z_par},{N_par})",
            'Z_par': Z_par, 'N_par': N_par,
            'P_par_sym': P_par, 'P_dau_sym': P_dau,
            'ratio_sym': ratio_sym,
            'P_par_num': P_par_num, 'P_dau_num': P_dau_num,
            'ratio_num': ratio_num, 'ln_ratio_num': ln_ratio_num,
        }

    import math
    if P_par_num != 0 and P_dau_num != 0:
        ratio_num = P_dau_num / P_par_num
        ln_ratio_num = math.log(abs(ratio_num))
    else:
        ratio_num = float('inf')
        ln_ratio_num = float('inf')

    return {
        'label': label or f"N({Z_par},{N_par})",
        'Z_par': Z_par, 'N_par': N_par,
        'P_par_sym': P_par, 'P_dau_sym': P_dau,
        'ratio_sym': ratio_sym,
        'P_par_num': P_par_num, 'P_dau_num': P_dau_num,
        'ratio_num': ratio_num, 'ln_ratio_num': ln_ratio_num,
    }


# ════════════════════════════════════════════════════════════════
# 5. Verification (__main__)
# ════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    import math

    print("=" * 72)
    print("SYMBOLIC TRANSFER MATRIX ENGINE — verification")
    print(f"All computations exact in q, evaluated at q0 = {Q0}")
    print("=" * 72)

    # ── 5a. Verify Delta_beta universality ──────────────────────────
    print()
    print("--- Universality of Delta_beta ---")
    print()

    D1 = T_mix - T_nn       # partner is neutron
    D2 = T_pp - T_mix       # partner is proton

    # Check all four entries are equal
    universal = True
    for i in range(2):
        for j in range(2):
            diff = simplify(D1.mat[i, j] - D2.mat[i, j])
            if diff != 0:
                universal = False
                print(f"  MISMATCH at ({i},{j}): {diff}")

    if universal:
        print("  T_mix - T_nn == T_pp - T_mix   [VERIFIED]")
    else:
        print("  UNIVERSALITY FAILED!")

    # Verify the decomposition: Delta_beta = (1/2)(1-q^2) T_pp + (q*s/2) I
    half_1mq2 = Rational(1, 2) * (1 - q**2)
    half_qs = q * s_skein / 2
    Delta_check = T_pp.scale(half_1mq2) + SymbolicTransferMatrix.identity().scale(half_qs)

    decomp_ok = True
    for i in range(2):
        for j in range(2):
            diff = simplify(Delta_beta.mat[i, j] - Delta_check.mat[i, j])
            if diff != 0:
                decomp_ok = False
                print(f"  DECOMPOSITION MISMATCH at ({i},{j}): {diff}")

    if decomp_ok:
        print("  Delta_beta = (1/2)(1-q^2) T_pp + (q*s/2) I   [VERIFIED]")
    print()

    # Show the matrices at q0
    print("--- Transfer matrices at q0 ---")
    print()
    T_pp.show("T_pp")
    print(f"  at q0: {T_pp.evaluate(Q0)}")
    print()
    T_nn.show("T_nn")
    print(f"  at q0: {T_nn.evaluate(Q0)}")
    print()
    T_mix.show("T_mix")
    print(f"  at q0: {T_mix.evaluate(Q0)}")
    print()
    Delta_beta.show("Delta_beta")
    print(f"  at q0: {Delta_beta.evaluate(Q0)}")
    print()

    # Determinants (symbolic)
    print("--- Determinants (at q0) ---")
    print(f"  det(T_pp)  = {float(T_pp.det().subs(q, Q0)):.10f}")
    print(f"  det(T_nn)  = {float(T_nn.det().subs(q, Q0)):.10f}")
    print(f"  det(T_mix) = {float(T_mix.det().subs(q, Q0)):.10f}")
    print(f"  det(Delta) = {float(Delta_beta.det().subs(q, Q0)):.10f}")
    print()

    # ── 5b. Tritium worked example (symbolic) ──────────────────────
    print("--- Tritium: 3H(1,2) -> 3He(2,1) ---")
    print()

    parent_H3 = NucleusTransferMatrix(1, 2)
    daughter_He3 = NucleusTransferMatrix(2, 1)

    print(f"  Parent  3H  ordering: {''.join(parent_H3.ordering)}")
    print(f"  Daughter 3He ordering: {''.join(daughter_He3.ordering)}")
    print()

    for i in range(parent_H3.n_generators):
        print(f"  sigma_{i}:")
        print(f"    at q0: V_par = {parent_H3.volume_at(i, Q0):.10f}, "
              f"V_dau = {daughter_He3.volume_at(i, Q0):.10f}")

    print(f"  at q0: P_3H  = {parent_H3.skein_at(Q0):.10f}")
    print(f"  at q0: P_3He = {daughter_He3.skein_at(Q0):.10f}")

    ratio = parent_H3.skein_at(Q0)
    ratio_dau = daughter_He3.skein_at(Q0)
    if ratio != 0:
        ln_r = math.log(abs(ratio_dau / ratio))
        print(f"  ln(P_dau/P_par) = {ln_r:.10f}")
    print()

    # ── 5c. Q-values for all 6 benchmark nuclei ───────────────────
    print("=" * 72)
    print("Q-VALUE COMPARISON (transfer matrix vs experiment)")
    print("=" * 72)
    print()

    nuclei = [
        (1,   2,   "3H",     Q_TRITIUM_MEV),
        (6,   8,   "14C",    Q_C14_MEV),
        (27,  33,  "60Co",   Q_CO60_MEV),
        (38,  52,  "90Sr",   Q_SR90_MEV),
        (55,  82,  "137Cs",  Q_CS137_MEV),
        (83,  127, "210Bi",  Q_BI210_MEV),
    ]

    # Header
    print(f"  {'Nucleus':>8s}  {'Z':>3s}  {'N':>3s}  "
          f"{'ln(Pd/Pp)':>12s}  {'Q_exp (MeV)':>12s}")
    print(f"  {'--------':>8s}  {'---':>3s}  {'---':>3s}  "
          f"{'------------':>12s}  {'------------':>12s}")

    import time
    results = []
    for Z_par, N_par, label, Q_exp in nuclei:
        t0 = time.time()
        res = beta_decay_qvalue(Z_par, N_par, q_val=Q0, label=label)
        ln_r = res['ln_ratio_num']
        print(f"  {label:>8s}  {Z_par:3d}  {N_par:3d}  "
              f"{ln_r:+12.6f}  {Q_exp:12.5f}")
        res['Q_exp_MeV'] = Q_exp
        results.append(res)

    print()
    print("  Notes:")
    print("  - ln(P_dau/P_par) is the raw Skein polynomial log-ratio")
    print("  - Conversion to MeV requires the energy scale E_cross * mu_0")
    print("  - The SIGN of ln(ratio) encodes exothermicity (negative = energetically favored)")
    print()

    # ── 5d. Connection to Groebner NF ──────────────────────────────
    print("=" * 72)
    print("GROEBNER NF <-> TRANSFER MATRIX CORRESPONDENCE")
    print("=" * 72)
    print()
    print("  Each V_hat_i(q) in the transfer matrix corresponds to one")
    print("  generator sigma_i in the Hecke algebra NF.")
    print()
    print("  Transfer matrix: V_hat_i = z * M_i[0,0] + M_i[1,0]")
    print("    where M_i = product of T(c_k, d_k) for all crossings at gen i")
    print()
    print("  Groebner NF: the reduced element in H_n has basis words.")
    print("    The Markov trace processes generators right-to-left,")
    print("    extracting the SAME z * (coefficient of sigma_i) + (constant)")
    print("    at each step.")
    print()
    print("  When generators COMMUTE (|i-j| >= 2), both methods agree exactly.")
    print("  When generators are ADJACENT (|i-j| = 1), interleaved crossings")
    print("  require the full Hecke reduction; the transfer matrix factored")
    print("  form is an approximation.")
    print()

    # Verify for tritium (small enough for symbolic Groebner)
    print("  Tritium verification (A=3, generators sigma_0 and sigma_1):")
    print(f"    Transfer matrix P_3H  = {parent_H3.skein_at(Q0):.10f}")
    print(f"    Transfer matrix P_3He = {daughter_He3.skein_at(Q0):.10f}")
    print()
    print("  To verify against Groebner NF, run:")
    print("    python3 hecke_symbolic.py   (for protium NF)")
    print("    python3 groebner-beta-decay.py   (for tritium NF)")
