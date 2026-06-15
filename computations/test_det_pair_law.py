"""pytest for the conjugate-pair determinant law helper."""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from det_pair_law import (  # noqa: E402
    det_pair_sign,
    det_rho,
    sweep_det_pair_law,
    syt_count,
    verify_det_pair_law,
)
from q_parameter import Q as Q0  # noqa: E402


# ── basic helpers ─────────────────────────────────────────

def test_syt_count_known_values():
    # |SYT(λ)| values from hook-length formula
    assert syt_count((1,)) == 1
    assert syt_count((2,)) == 1
    assert syt_count((1, 1)) == 1
    assert syt_count((2, 1)) == 2
    assert syt_count((3, 2, 1)) == 16    # standard tableaux of staircase ρ_3


def test_det_pair_sign_parity():
    # (L · dim_λ) mod 2 → ±1
    assert det_pair_sign((2, 1), 0) == 1     # 0 · anything is even
    assert det_pair_sign((2, 1), 1) == 1     # dim=2 even ⇒ even product
    assert det_pair_sign((1, 1, 1), 1) == -1  # dim=1, L=1 ⇒ odd
    assert det_pair_sign((1, 1, 1), 2) == 1   # dim=1, L=2 ⇒ even


# ── identity word ─────────────────────────────────────────

def test_det_rho_identity_is_one():
    # Empty word = identity matrix; det = 1 for any non-empty rep
    for lam in [(2, 1), (1, 1, 1), (3,), (2, 2)]:
        d = det_rho(lam, (), Q0)
        assert math.isclose(d, 1.0, abs_tol=1e-10), \
            f"det ρ_{lam}(e) = {d} ≠ 1"


# ── full sweep across n=3..6 ──────────────────────────────

def test_sweep_n3():
    words = [(), (0,), (1,), (0, 1), (1, 0, 1)]
    report = sweep_det_pair_law(3, words, Q0)
    assert report["all_pass"], report


def test_sweep_n4():
    words = [(), (0, 1, 2), (1, 2, 1), (0, 1, 0, 2), (0, 1, 2, 1, 0)]
    report = sweep_det_pair_law(4, words, Q0)
    assert report["all_pass"], report


def test_sweep_n5():
    words = [(), (0, 1, 2, 3), (1, 2, 3, 2, 1), (0, 0, 1, 1)]
    report = sweep_det_pair_law(5, words, Q0)
    assert report["all_pass"], report


def test_sweep_n6():
    words = [(), (0, 1, 2, 3, 4), (0, 2, 4), (1, 2, 3, 4, 0, 1)]
    report = sweep_det_pair_law(6, words, Q0)
    assert report["all_pass"], report


# ── verify_det_pair_law on individual pairs ───────────────

def test_verify_returns_predicted_actual_pass():
    pred, actual, passes = verify_det_pair_law((3, 1), (0, 1, 2), Q0)
    assert passes, f"law fails for λ=(3,1), w=(0,1,2): pred={pred}, actual={actual}"
    # sign of actual must match prediction
    assert (actual > 0) == (pred > 0)


def test_self_conjugate_lambda_is_trivially_consistent():
    """For self-conjugate λ, λ' = λ, so the product is det²(ρ_λ(w)) ≥ 0."""
    for w in [(), (0,), (0, 1), (1, 0, 1)]:
        _, actual, _ = verify_det_pair_law((2, 1), w, Q0)
        if not math.isnan(actual):
            assert actual >= -1e-9, \
                f"det²ρ_(2,1)({w}) = {actual} < 0 (self-conjugate must be ≥0)"


def test_pair_count_matches_partition_split():
    """At n=4, p(4)=5 partitions: (4),(3,1),(2,2),(2,1,1),(1,1,1,1).
    (2,2) is self-conjugate ⇒ 1 self-conj + 2 ordered pairs."""
    report = sweep_det_pair_law(4, [()], Q0)
    assert len(report["self_conjugate"]) == 1
    assert report["pair_count"] == 2


def test_pair_count_n5():
    """At n=5, p(5)=7. Self-conj: (3,1,1) ⇒ 1 self + 3 ordered pairs."""
    report = sweep_det_pair_law(5, [()], Q0)
    assert len(report["self_conjugate"]) == 1
    assert report["pair_count"] == 3
