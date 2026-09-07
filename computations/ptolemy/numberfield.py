"""A minimal exact number field K = Q[T]/(f), as dense coefficient vectors.

WHY NOT sympy expressions.  The first attempt at the character computation carried K
elements as sympy expressions in T and reduced with sp.rem(sp.Poly(...), ...) after
every operation.  That ran at 100% CPU for 17 minutes on a 3x3 matrix product without
emitting a line: each op re-parses, re-expands and re-canonicalises an expression tree
whose rational coefficients here run to twelve digits.  An element of a degree-d field
is d rationals; representing it as anything else is what costs.

An element is a tuple of exactly deg(f) Fractions, low degree first.  Multiplication is
a convolution followed by reduction against a precomputed table of T^k for
k = d .. 2d-2, so no polynomial division happens at runtime.  Inversion is the extended
Euclidean algorithm on Q[T], which is where the only real work is and is rare.

Exact throughout: Fraction only.  There is no float anywhere in this module, and
equality is equality, never a tolerance.
"""
from fractions import Fraction


class NumberField:
    def __init__(self, coeffs):
        """coeffs: the monic-or-not minimal polynomial, LOW degree first."""
        c = [Fraction(x) for x in coeffs]
        while c and c[-1] == 0:
            c.pop()
        self.deg = len(c) - 1
        if self.deg < 1:
            raise ValueError("minimal polynomial must have degree >= 1")
        lead = c[-1]
        self.f = [x / lead for x in c]                 # monic
        # T^d = -(f_0 + f_1 T + ... + f_{d-1} T^{d-1})
        self.pow = {self.deg: [-x for x in self.f[:self.deg]]}
        for k in range(self.deg + 1, 2 * self.deg - 1):
            prev = self.pow[k - 1]
            shifted = [Fraction(0)] + prev[:-1]
            top = prev[-1]
            self.pow[k] = [a + top * b for a, b in zip(shifted, self.pow[self.deg])]

    # --- constructors -------------------------------------------------
    def zero(self):
        return tuple(Fraction(0) for _ in range(self.deg))

    def one(self):
        return self.const(1)

    def const(self, x):
        v = [Fraction(0)] * self.deg
        v[0] = Fraction(x)
        return tuple(v)

    def gen(self):
        v = [Fraction(0)] * self.deg
        v[1 % self.deg] = Fraction(1)
        return tuple(v)

    def from_poly_coeffs(self, coeffs):
        """coeffs low-degree-first, any length; reduced into K."""
        acc = list(self.zero())
        for k, c in enumerate(coeffs):
            c = Fraction(c)
            if c == 0:
                continue
            if k < self.deg:
                acc[k] += c
            else:
                for i, b in enumerate(self._reduce_power(k)):
                    acc[i] += c * b
        return tuple(acc)

    def _reduce_power(self, k):
        if k in self.pow:
            return self.pow[k]
        cur = self.pow[max(self.pow)]
        for _ in range(max(self.pow), k):
            shifted = [Fraction(0)] + cur[:-1]
            top = cur[-1]
            cur = [a + top * b for a, b in zip(shifted, self.pow[self.deg])]
        self.pow[k] = cur
        return cur

    # --- arithmetic ---------------------------------------------------
    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def mul(self, a, b):
        d = self.deg
        conv = [Fraction(0)] * (2 * d - 1)
        for i, x in enumerate(a):
            if x == 0:
                continue
            for j, y in enumerate(b):
                if y == 0:
                    continue
                conv[i + j] += x * y
        acc = list(conv[:d])
        for k in range(d, 2 * d - 1):
            c = conv[k]
            if c == 0:
                continue
            for i, b_ in enumerate(self._reduce_power(k)):
                acc[i] += c * b_
        return tuple(acc)

    def inv(self, a):
        """Extended Euclid in Q[T].  Raises if a is a zero divisor (f reducible)."""
        if all(x == 0 for x in a):
            raise ZeroDivisionError("zero is not invertible in K")
        r0, r1 = list(self.f), self._trim(list(a))
        s0, s1 = [Fraction(0)], [Fraction(1)]
        while any(x != 0 for x in r1):
            q, rem = self._divmod(r0, r1)
            r0, r1 = r1, self._trim(rem)
            s0, s1 = s1, self._trim(self._polysub(s0, self._polymul(q, s1)))
        if len(r0) != 1 or r0[0] == 0:
            raise ZeroDivisionError(f"not invertible: gcd has degree {len(r0) - 1}"
                                    " -- the minimal polynomial is reducible")
        return self.from_poly_coeffs([x / r0[0] for x in s0])

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def is_zero(self, a):
        return all(x == 0 for x in a)

    def eq(self, a, b):
        return all(x == y for x, y in zip(a, b))

    # --- bare Q[T] helpers, low degree first --------------------------
    @staticmethod
    def _trim(p):
        p = list(p)
        while len(p) > 1 and p[-1] == 0:
            p.pop()
        return p

    @staticmethod
    def _polymul(a, b):
        out = [Fraction(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] += x * y
        return out

    @staticmethod
    def _polysub(a, b):
        n = max(len(a), len(b))
        a = list(a) + [Fraction(0)] * (n - len(a))
        b = list(b) + [Fraction(0)] * (n - len(b))
        return [x - y for x, y in zip(a, b)]

    def _divmod(self, a, b):
        a, b = list(a), self._trim(list(b))
        q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
        while len(a) >= len(b) and any(x != 0 for x in a):
            a = self._trim(a)
            if len(a) < len(b):
                break
            shift = len(a) - len(b)
            c = a[-1] / b[-1]
            q[shift] += c
            for i, y in enumerate(b):
                a[i + shift] -= c * y
            a = self._trim(a)
        return q, a
