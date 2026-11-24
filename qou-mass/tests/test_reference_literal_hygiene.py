"""Regression tests for qou-mass reference-literal hygiene at >= 80 dps (qou-4w7k)."""
from __future__ import annotations

from decimal import Decimal
import unittest

import mpmath as mp

import qou_mass as qm
from qou_mass import daha_macdonald, demazure, toroidal_harmonic, wenzl_qpoch
from qou_mass._internal import y_lambda_su_n as y_su_n
from qou_mass._internal.codata_constants import U_MEV
from qou_mass._internal.q_parameter import Q_50_DIGIT_STR


class TestReferenceLiteralHygiene(unittest.TestCase):
    def test_mass_excess_uses_codata_2022_u_mev_at_80dps(self):
        with mp.workdps(80):
            m_4he = qm.predict("4He", observable="mass").value
            excess_4he = qm.predict("4He", observable="mass_excess").value
            u_dec = Decimal(mp.nstr(U_MEV, 20, strip_zeros=True))
            self.assertEqual(excess_4he, m_4he - Decimal(4) * u_dec)

    def test_y_lambda_su_n_registry_constants_derived_at_80dps(self):
        with mp.workdps(80):
            q = mp.mpf(Q_50_DIGIT_STR)
            y3 = y_su_n.y_lambda_su_n(3, q, 2)
            self.assertLess(abs(y3[(3,)] - y_su_n.REG_D[0]), mp.mpf("1e-70"))
            self.assertLess(abs(y3[(2, 1)] - y_su_n.REG_D[1]), mp.mpf("1e-70"))
            self.assertEqual(y3[(1, 1, 1)], mp.mpf(0))
            z_d = y_su_n.z_from_weights(q, y_su_n.y_lambda_su_n(2, q, 2))
            self.assertLess(abs(z_d - y_su_n.REG_ZD), mp.mpf("1e-70"))
            self.assertGreater(abs(z_d - y_su_n.REG_ZC), mp.mpf("0.1"))

    def test_auxiliary_qou_mass_modules_use_mpf_at_80dps(self):
        with mp.workdps(80):
            q0 = mp.mpf(Q_50_DIGIT_STR)
            p_eval = daha_macdonald.macdonald_principal_eval([2], q0, q0 ** 2)
            self.assertIsInstance(p_eval, mp.mpf)

            qp = wenzl_qpoch.q_pochhammer(q0, 2)
            tr_p2 = wenzl_qpoch.wenzl_p2_trace(q0, N=2)
            self.assertIsInstance(qp, mp.mpf)
            self.assertIsInstance(tr_p2, mp.mpf)
            self.assertLess(abs(tr_p2 - (q0 ** 2 + 1 + q0 ** (-2))), mp.mpf("1e-70"))

            cosh_eta = (q0 + mp.mpf(1) / q0) / mp.mpf(2)
            th_p = toroidal_harmonic.toroidal_harmonic_P(0, 1, cosh_eta)
            th_q = toroidal_harmonic.toroidal_harmonic_Q(0, 1, cosh_eta)
            self.assertIsInstance(th_p, mp.mpf)
            self.assertIsInstance(th_q, mp.mpf)

            dem = demazure.compute_coefficients(3, (1, 0, 0), q0, eval_point="principal")
            self.assertTrue(all(isinstance(v, mp.mpf) for v in dem.values()))


if __name__ == "__main__":
    unittest.main()
