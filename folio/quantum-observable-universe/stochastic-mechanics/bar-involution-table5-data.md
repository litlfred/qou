| Combination | Result | Lean theorem |
|---|---|---|
| sym + sym | sym | `IsBarSymmetric.add` |
| sym $\times$ sym | sym | `IsBarSymmetric.mul` |
| anti + anti | anti | `IsBarAntiSymmetric.add` |
| **anti $\times$ anti** | **sym** | `IsBarSymmetric.of_mul_antisym` |
| sym $\times$ anti | anti | `IsBarAntiSymmetric.of_sym_mul` |
| $-$sym | sym | `IsBarSymmetric.neg` |
| $-$anti | anti | `IsBarAntiSymmetric.neg` |
| $h^{2n}$ (h anti) | sym | `IsBarAntiSymmetric.pow_two_mul` |
| $h^{2n+1}$ (h anti) | anti | `IsBarAntiSymmetric.pow_two_mul_add_one` |
| $\mathrm{bar}(-x) = -\mathrm{bar}(x)$ | identity | `bar_neg` |
