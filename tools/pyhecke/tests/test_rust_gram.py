"""Integration: Rust `hecke-gram` vs Python `pyhecke.gram.G`.

Schema-contract and Python-mirror checks run UNCONDITIONALLY in every
environment (bean `qou-mt4n`), so a schema/struct key break or a convention-D
quotient-inverse violation cannot hide behind an unbuilt Rust binary. Only the
tests that invoke the compiled `hecke-gram` subprocess are skipped when the
release binary is absent.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from pyhecke import bridge

_HECKE_ENGINE_DIR = Path(__file__).resolve().parents[2] / "hecke-engine"
_SCHEMA_PATH = _HECKE_ENGINE_DIR / "schemas" / "gram.schema.json"
_GRAM_RS_PATH = _HECKE_ENGINE_DIR / "src" / "gram.rs"


def _rust_gram_available() -> bool:
    return bridge.binary_path("hecke-gram") is not None


_requires_rust_gram = pytest.mark.skipif(
    not _rust_gram_available(),
    reason="hecke-gram binary not built (run `cargo build --release` in tools/hecke-engine/)",
)


def _load_gram_schema() -> dict:
    with _SCHEMA_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def test_gram_schema_is_valid_and_requires_convention_d_keys():
    """Unconditional schema check (bean qou-mt4n): gram.schema.json must be a
    valid Draft 2020-12 schema requiring `quotient_inverse` + `radical` and
    excluding the pre-convention-D `inverse` key."""
    import jsonschema

    schema = _load_gram_schema()
    jsonschema.Draft202012Validator.check_schema(schema)
    required = set(schema.get("required", []))
    props = set(schema.get("properties", {}).keys())
    assert "quotient_inverse" in required
    assert "radical" in required
    assert "inverse" not in required
    assert "inverse" not in props
    assert required == props


def test_rust_gram_struct_fields_match_schema_contract():
    """Unconditional source-to-schema contract check (bean qou-mt4n): the
    serialized fields of `pub struct GramCertificate` in `src/gram.rs` must
    match `gram.schema.json` even when the Rust binary is not compiled."""
    schema = _load_gram_schema()
    src = _GRAM_RS_PATH.read_text(encoding="utf-8")
    m = re.search(r"pub\s+struct\s+GramCertificate\s*\{([^}]*)\}", src, re.DOTALL)
    assert m is not None, "pub struct GramCertificate not found in tools/hecke-engine/src/gram.rs"
    struct_fields = set(re.findall(r"pub\s+([a-zA-Z0-9_]+)\s*:", m.group(1)))
    assert struct_fields == set(schema["required"]), (
        f"GramCertificate fields {sorted(struct_fields)} != "
        f"schema required {sorted(schema['required'])}"
    )
    assert "inverse" not in struct_fields


def test_python_gram_certificate_validates_against_schema():
    """Unconditional Python-mirror contract check (bean qou-mt4n): a
    certificate assembled from `pyhecke.gram` validates against
    `gram.schema.json` and satisfies the convention-D quotient-inverse and
    radical identities (`G @ rad = 0`, `G_pinv @ rad = 0`, `G @ G_pinv @ G = G`)."""
    import jsonschema
    import numpy as np

    from pyhecke import gram as pg

    schema = _load_gram_schema()
    G = np.asarray(pg.G, dtype=float)
    GP = np.linalg.pinv(G)
    # Closed-form three-strand q-antisymmetriser (-1/q)^len(w) on NF_BASIS
    lengths = [len(w) for w in pg.NF_BASIS]
    rad = np.array([(-1.0 / float(pg.q0)) ** k for k in lengths], dtype=float)

    cert = {
        "q": float(pg.q0),
        "z": float(pg.z),
        "h": float(pg.h),
        "n": 3,
        "basis": list(pg.NF_NAMES),
        "trace_weights": [float(x) for x in pg.TR_M],
        "matrix": G.tolist(),
        "quotient_inverse": GP.tolist(),
        "radical": rad.tolist(),
        "determinant": float(np.linalg.det(G)),
    }
    jsonschema.validate(cert, schema)
    assert np.linalg.norm(G @ rad) < 1e-10
    assert np.linalg.norm(GP @ rad) < 1e-10
    assert np.allclose(G @ GP @ G, G, atol=1e-10)


@_requires_rust_gram
def test_rust_gram_validates_against_schema():
    """Rust output must validate against gram.schema.json."""
    import jsonschema

    cert = bridge.gram_from_rust()
    schema = _load_gram_schema()
    jsonschema.validate(cert, schema)


@_requires_rust_gram
def test_rust_and_python_gram_agree():
    """Rust and Python Gram matrices must agree at f64 precision."""
    import numpy as np

    from pyhecke import gram as pg

    rust_G = bridge.gram_matrix_from_rust()
    py_G = pg.G
    assert rust_G.shape == py_G.shape == (6, 6)
    max_diff = np.max(np.abs(rust_G - py_G))
    assert max_diff < 1e-14, f"Rust and Python Gram disagree: max diff {max_diff:.2e}"


@_requires_rust_gram
def test_rust_gram_det_matches_python():
    import numpy as np

    from pyhecke import gram as pg

    cert = bridge.gram_from_rust()
    py_det = np.linalg.det(pg.G)
    rust_det = cert["determinant"]
    assert abs(rust_det - py_det) < 1e-10


@_requires_rust_gram
def test_rust_cert_has_no_full_inverse_and_quotient_inverse_kills_the_radical():
    """Under convention D there is NO 6x6 inverse, so the certificate must not
    offer one, and what it does offer must be the inverse on the quotient.

    This replaces `test_rust_gram_inverse_is_right_inverse`, which asserted
    `G @ cert["inverse"] == I`. That identity is FALSE under convention D — the
    form is singular (corank 1, the three-strand q-antisymmetriser; det = 0
    exactly over Q(q), see computations/probes/gram_radical_cellular_revalidation.py).
    The old test survived the C -> D migration only because the whole module
    skips when the Rust binary is not built, so it never ran to fail. Its key
    `cert["inverse"]` no longer exists either — the field was renamed to
    `quotient_inverse` deliberately, so that a stale consumer breaks loudly."""
    import numpy as np

    cert = bridge.gram_from_rust()
    assert "inverse" not in cert, (
        "`inverse` must not be resurrected: under convention D the 6x6 inverse "
        "does not exist, and a field by that name would name a nonexistent object"
    )
    G = np.array(cert["matrix"])
    GP = np.array(cert["quotient_inverse"])
    rad = np.array(cert["radical"])

    # the radical really is a null direction of G
    assert np.linalg.norm(G @ rad) < 1e-10
    # the quotient inverse annihilates it too — that is what makes it the
    # inverse ON THE QUOTIENT rather than an approximation to a missing inverse
    assert np.linalg.norm(GP @ rad) < 1e-10
    # and on the complement of the radical it does invert: G·GP·G = G
    assert np.allclose(G @ GP @ G, G, atol=1e-10)


@_requires_rust_gram
def test_rust_gram_at_custom_q():
    """Different q values produce different G matrices."""
    import numpy as np

    c0 = bridge.gram_from_rust(q=1.10)
    c1 = bridge.gram_from_rust(q=1.20)
    G0 = np.array(c0["matrix"])
    G1 = np.array(c1["matrix"])
    assert not np.allclose(G0, G1)
