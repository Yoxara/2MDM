# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Fri 2 Aug 2024 17:01:18


from object_library import all_decays, Decay
import particles as P


Decay_h = Decay(name = 'Decay_h',
                particle = P.h,
                partial_widths = {(P.Sd,P.Sd):'((cosa**6*lam3**2*vev**2 + 12*cosa**4*lam1*lam3*sina**2*vev**2 - 4*cosa**4*lam3**2*sina**2*vev**2 + 36*cosa**2*lam1**2*sina**4*vev**2 - 24*cosa**2*lam1*lam3*sina**4*vev**2 + 4*cosa**2*lam3**2*sina**4*vev**2 - 12*cosa**5*lam2*lam3*sina*vev*vev2 + 4*cosa**5*lam3**2*sina*vev*vev2 - 72*cosa**3*lam1*lam2*sina**3*vev*vev2 + 24*cosa**3*lam1*lam3*sina**3*vev*vev2 + 24*cosa**3*lam2*lam3*sina**3*vev*vev2 - 10*cosa**3*lam3**2*sina**3*vev*vev2 - 12*cosa*lam1*lam3*sina**5*vev*vev2 + 4*cosa*lam3**2*sina**5*vev*vev2 + 36*cosa**4*lam2**2*sina**2*vev2**2 - 24*cosa**4*lam2*lam3*sina**2*vev2**2 + 4*cosa**4*lam3**2*sina**2*vev2**2 + 12*cosa**2*lam2*lam3*sina**4*vev2**2 - 4*cosa**2*lam3**2*sina**4*vev2**2 + lam3**2*sina**6*vev2**2)*cmath.sqrt(Mh**4 - 4*Mh**2*MSd**2))/(32.*cmath.pi*abs(Mh)**3)',
                                  (P.chi,P.chi):'((-4*Mchi**2*sina**2*ychi**2 + Mh**2*sina**2*ychi**2)*cmath.sqrt(-4*Mchi**2*Mh**2 + Mh**4))/(32.*cmath.pi*abs(Mh)**3)',
                                  (P.b,P.b__tilde__):'((-12*cosa**2*MB**2*yb**2 + 3*cosa**2*Mh**2*yb**2)*cmath.sqrt(-4*MB**2*Mh**2 + Mh**4))/(16.*cmath.pi*abs(Mh)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((cosa**2*Mh**2*ytau**2 - 4*cosa**2*MTA**2*ytau**2)*cmath.sqrt(Mh**4 - 4*Mh**2*MTA**2))/(16.*cmath.pi*abs(Mh)**3)',
                                  (P.t,P.t__tilde__):'((3*cosa**2*Mh**2*yt**2 - 12*cosa**2*MT**2*yt**2)*cmath.sqrt(Mh**4 - 4*Mh**2*MT**2))/(16.*cmath.pi*abs(Mh)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*cosa**2*ee**4*vev**2)/(4.*sw**4) + (cosa**2*ee**4*Mh**4*vev**2)/(16.*MW**4*sw**4) - (cosa**2*ee**4*Mh**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(Mh**4 - 4*Mh**2*MW**2))/(16.*cmath.pi*abs(Mh)**3)',
                                  (P.Z,P.Z):'(((9*cosa**2*ee**4*vev**2)/2. + (3*cosa**2*ee**4*Mh**4*vev**2)/(8.*MZ**4) - (3*cosa**2*ee**4*Mh**2*vev**2)/(2.*MZ**2) + (3*cosa**2*cw**4*ee**4*vev**2)/(4.*sw**4) + (cosa**2*cw**4*ee**4*Mh**4*vev**2)/(16.*MZ**4*sw**4) - (cosa**2*cw**4*ee**4*Mh**2*vev**2)/(4.*MZ**2*sw**4) + (3*cosa**2*cw**2*ee**4*vev**2)/sw**2 + (cosa**2*cw**2*ee**4*Mh**4*vev**2)/(4.*MZ**4*sw**2) - (cosa**2*cw**2*ee**4*Mh**2*vev**2)/(MZ**2*sw**2) + (3*cosa**2*ee**4*sw**2*vev**2)/cw**2 + (cosa**2*ee**4*Mh**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (cosa**2*ee**4*Mh**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*cosa**2*ee**4*sw**4*vev**2)/(4.*cw**4) + (cosa**2*ee**4*Mh**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (cosa**2*ee**4*Mh**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(Mh**4 - 4*Mh**2*MZ**2))/(32.*cmath.pi*abs(Mh)**3)',
                                  (P.Zp,P.Zp):'((12*gZp**4*QBphi**4*sina**2*vev2**2 + (gZp**4*Mh**4*QBphi**4*sina**2*vev2**2)/MZp**4 - (4*gZp**4*Mh**2*QBphi**4*sina**2*vev2**2)/MZp**2)*cmath.sqrt(Mh**4 - 4*Mh**2*MZp**2))/(32.*cmath.pi*abs(Mh)**3)'})

Decay_Sd = Decay(name = 'Decay_Sd',
                 particle = P.Sd,
                 partial_widths = {(P.h,P.h):'((36*cosa**4*lam1**2*sina**2*vev**2 - 24*cosa**4*lam1*lam3*sina**2*vev**2 + 4*cosa**4*lam3**2*sina**2*vev**2 + 12*cosa**2*lam1*lam3*sina**4*vev**2 - 4*cosa**2*lam3**2*sina**4*vev**2 + lam3**2*sina**6*vev**2 + 12*cosa**5*lam1*lam3*sina*vev*vev2 - 4*cosa**5*lam3**2*sina*vev*vev2 + 72*cosa**3*lam1*lam2*sina**3*vev*vev2 - 24*cosa**3*lam1*lam3*sina**3*vev*vev2 - 24*cosa**3*lam2*lam3*sina**3*vev*vev2 + 10*cosa**3*lam3**2*sina**3*vev*vev2 + 12*cosa*lam2*lam3*sina**5*vev*vev2 - 4*cosa*lam3**2*sina**5*vev*vev2 + cosa**6*lam3**2*vev2**2 + 12*cosa**4*lam2*lam3*sina**2*vev2**2 - 4*cosa**4*lam3**2*sina**2*vev2**2 + 36*cosa**2*lam2**2*sina**4*vev2**2 - 24*cosa**2*lam2*lam3*sina**4*vev2**2 + 4*cosa**2*lam3**2*sina**4*vev2**2)*cmath.sqrt(-4*Mh**2*MSd**2 + MSd**4))/(32.*cmath.pi*abs(MSd)**3)',
                                   (P.chi,P.chi):'((-4*cosa**2*Mchi**2*ychi**2 + cosa**2*MSd**2*ychi**2)*cmath.sqrt(-4*Mchi**2*MSd**2 + MSd**4))/(32.*cmath.pi*abs(MSd)**3)',
                                   (P.b,P.b__tilde__):'((-12*MB**2*sina**2*yb**2 + 3*MSd**2*sina**2*yb**2)*cmath.sqrt(-4*MB**2*MSd**2 + MSd**4))/(16.*cmath.pi*abs(MSd)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((MSd**2*sina**2*ytau**2 - 4*MTA**2*sina**2*ytau**2)*cmath.sqrt(MSd**4 - 4*MSd**2*MTA**2))/(16.*cmath.pi*abs(MSd)**3)',
                                   (P.t,P.t__tilde__):'((3*MSd**2*sina**2*yt**2 - 12*MT**2*sina**2*yt**2)*cmath.sqrt(MSd**4 - 4*MSd**2*MT**2))/(16.*cmath.pi*abs(MSd)**3)',
                                   (P.W__minus__,P.W__plus__):'(((3*ee**4*sina**2*vev**2)/(4.*sw**4) + (ee**4*MSd**4*sina**2*vev**2)/(16.*MW**4*sw**4) - (ee**4*MSd**2*sina**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MSd**4 - 4*MSd**2*MW**2))/(16.*cmath.pi*abs(MSd)**3)',
                                   (P.Z,P.Z):'(((9*ee**4*sina**2*vev**2)/2. + (3*ee**4*MSd**4*sina**2*vev**2)/(8.*MZ**4) - (3*ee**4*MSd**2*sina**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*sina**2*vev**2)/(4.*sw**4) + (cw**4*ee**4*MSd**4*sina**2*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MSd**2*sina**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*sina**2*vev**2)/sw**2 + (cw**2*ee**4*MSd**4*sina**2*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MSd**2*sina**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sina**2*sw**2*vev**2)/cw**2 + (ee**4*MSd**4*sina**2*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MSd**2*sina**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sina**2*sw**4*vev**2)/(4.*cw**4) + (ee**4*MSd**4*sina**2*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MSd**2*sina**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MSd**4 - 4*MSd**2*MZ**2))/(32.*cmath.pi*abs(MSd)**3)',
                                   (P.Zp,P.Zp):'((12*cosa**2*gZp**4*QBphi**4*vev2**2 + (cosa**2*gZp**4*MSd**4*QBphi**4*vev2**2)/MZp**4 - (4*cosa**2*gZp**4*MSd**2*QBphi**4*vev2**2)/MZp**2)*cmath.sqrt(MSd**4 - 4*MSd**2*MZp**2))/(32.*cmath.pi*abs(MSd)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-0.5*(ee**2*MTA**2)/sw**2 - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_Zp = Decay(name = 'Decay_Zp',
                 particle = P.Zp,
                 partial_widths = {(P.u,P.u__tilde__):'(gZp**2*MZp**4*QBq**2)/(4.*cmath.pi*abs(MZp)**3)',
                                   (P.c,P.c__tilde__):'(gZp**2*MZp**4*QBq**2)/(4.*cmath.pi*abs(MZp)**3)',
                                   (P.t,P.t__tilde__):'((24*gZp**2*MT**2*QBq**2 + 12*gZp**2*MZp**2*QBq**2)*cmath.sqrt(-4*MT**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.d,P.d__tilde__):'(gZp**2*MZp**4*QBq**2)/(4.*cmath.pi*abs(MZp)**3)',
                                   (P.s,P.s__tilde__):'(gZp**2*MZp**4*QBq**2)/(4.*cmath.pi*abs(MZp)**3)',
                                   (P.b,P.b__tilde__):'((24*gZp**2*MB**2*QBq**2 + 12*gZp**2*MZp**2*QBq**2)*cmath.sqrt(-4*MB**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.chi,P.chi):'((-16*gchi**2*Mchi**2 + 4*gchi**2*MZp**2)*cmath.sqrt(-4*Mchi**2*MZp**2 + MZp**4))/(96.*cmath.pi*abs(MZp)**3)'})
