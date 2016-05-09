Minimize
  7 xAB0 + 7 xAB1 + 7 xAB2 + 7 xAB3 + 7 xAB4 + 3 xAC0 + 3 xAC1 + 3 xAC2
   + 3 xAC3 + 3 xAC4 + 7 xBA0 + 7 xBA1 + 7 xBA2 + 7 xBA3 + 7 xBA4 + 6 xBC0
   + 6 xBC1 + 6 xBC2 + 6 xBC3 + 6 xBC4 + 3 xCA0 + 3 xCA1 + 3 xCA2 + 3 xCA3
   + 3 xCA4 + 6 xCB0 + 6 xCB1 + 6 xCB2 + 6 xCB3 + 6 xCB4 + 10 zA0 + 10 zA1
   + 10 zA2 + 10 zA3 + 10 zA4 + 10 zB0 + 10 zB1 + 10 zB2 + 10 zB3 + 10 zB4
   + 10 zC0 + 10 zC1 + 10 zC2 + 10 zC3 + 10 zC4
Subject To
 cargo_flow_balance_AB1: yAB0 - uAB0 + uAB1 = 10
 cargo_flow_balance_AB2: yAB1 - uAB1 + uAB2 = 20
 cargo_flow_balance_AB3: yAB2 - uAB2 + uAB3 = 10
 cargo_flow_balance_AB4: yAB3 - uAB3 + uAB4 = 40
 cargo_flow_balance_AC1: yAC0 - uAC0 + uAC1 = 5
 cargo_flow_balance_AC2: yAC1 - uAC1 + uAC2 = 5
 cargo_flow_balance_AC3: yAC2 - uAC2 + uAC3 = 5
 cargo_flow_balance_AC4: yAC3 - uAC3 + uAC4 = 5
 cargo_flow_balance_BA1: yBA0 - uBA0 + uBA1 = 2.5
 cargo_flow_balance_BA2: yBA1 - uBA1 + uBA2 = 2.5
 cargo_flow_balance_BA3: yBA2 - uBA2 + uBA3 = 2.5
 cargo_flow_balance_BA4: yBA3 - uBA3 + uBA4 = 2.5
 cargo_flow_balance_BC1: yBC0 - uBC0 + uBC1 = 2.5
 cargo_flow_balance_BC2: yBC1 - uBC1 + uBC2 = 2.5
 cargo_flow_balance_BC3: yBC2 - uBC2 + uBC3 = 2.5
 cargo_flow_balance_BC4: yBC3 - uBC3 + uBC4 = 2.5
 cargo_flow_balance_CA1: yCA0 - uCA0 + uCA1 = 4
 cargo_flow_balance_CA2: yCA1 - uCA1 + uCA2 = 4
 cargo_flow_balance_CA3: yCA2 - uCA2 + uCA3 = 4
 cargo_flow_balance_CA4: yCA3 - uCA3 + uCA4 = 4
 cargo_flow_balance_CB1: yCB0 - uCB0 + uCB1 = 40
 cargo_flow_balance_CB2: yCB1 - uCB1 + uCB2 = 20
 cargo_flow_balance_CB3: yCB2 - uCB2 + uCB3 = 30
 cargo_flow_balance_CB4: yCB3 - uCB3 + uCB4 = 20
 planes_flow_balance_A1: xAB1 + xAC1 - xBA0 - xCA0 + yAB1 + yAC1 - yBA0
   - yCA0 - zA0 + zA1 = 0
 planes_flow_balance_A2: xAB2 + xAC2 - xBA1 - xCA1 + yAB2 + yAC2 - yBA1
   - yCA1 - zA1 + zA2 = 0
 planes_flow_balance_A3: xAB3 + xAC3 - xBA2 - xCA2 + yAB3 + yAC3 - yBA2
   - yCA2 - zA2 + zA3 = 0
 planes_flow_balance_A4: xAB4 + xAC4 - xBA3 - xCA3 + yAB4 + yAC4 - yBA3
   - yCA3 - zA3 + zA4 = 0
 planes_flow_balance_B1: - xAB0 + xBA1 + xBC1 - xCB0 - yAB0 + yBA1 + yBC1
   - yCB0 - zB0 + zB1 = 0
 planes_flow_balance_B2: - xAB1 + xBA2 + xBC2 - xCB1 - yAB1 + yBA2 + yBC2
   - yCB1 - zB1 + zB2 = 0
 planes_flow_balance_B3: - xAB2 + xBA3 + xBC3 - xCB2 - yAB2 + yBA3 + yBC3
   - yCB2 - zB2 + zB3 = 0
 planes_flow_balance_B4: - xAB3 + xBA4 + xBC4 - xCB3 - yAB3 + yBA4 + yBC4
   - yCB3 - zB3 + zB4 = 0
 planes_flow_balance_C1: - xAC0 - xBC0 + xCA1 + xCB1 - yAC0 - yBC0 + yCA1
   + yCB1 - zC0 + zC1 = 0
 planes_flow_balance_C2: - xAC1 - xBC1 + xCA2 + xCB2 - yAC1 - yBC1 + yCA2
   + yCB2 - zC1 + zC2 = 0
 planes_flow_balance_C3: - xAC2 - xBC2 + xCA3 + xCB3 - yAC2 - yBC2 + yCA3
   + yCB3 - zC2 + zC3 = 0
 planes_flow_balance_C4: - xAC3 - xBC3 + xCA4 + xCB4 - yAC3 - yBC3 + yCA4
   + yCB4 - zC3 + zC4 = 0
 cargo_planes_constraint_for_pair_AB_on_day_0: yAB0 - uAB0 <= 10
 cargo_planes_constraint_for_pair_AB_on_day_1: yAB1 - uAB1 <= 20
 cargo_planes_constraint_for_pair_AB_on_day_2: yAB2 - uAB2 <= 10
 cargo_planes_constraint_for_pair_AB_on_day_3: yAB3 - uAB3 <= 40
 cargo_planes_constraint_for_pair_AB_on_day_4: yAB4 - uAB4 <= 30
 cargo_planes_constraint_for_pair_AC_on_day_0: yAC0 - uAC0 <= 5
 cargo_planes_constraint_for_pair_AC_on_day_1: yAC1 - uAC1 <= 5
 cargo_planes_constraint_for_pair_AC_on_day_2: yAC2 - uAC2 <= 5
 cargo_planes_constraint_for_pair_AC_on_day_3: yAC3 - uAC3 <= 5
 cargo_planes_constraint_for_pair_AC_on_day_4: yAC4 - uAC4 <= 5
 cargo_planes_constraint_for_pair_BA_on_day_0: yBA0 - uBA0 <= 2.5
 cargo_planes_constraint_for_pair_BA_on_day_1: yBA1 - uBA1 <= 2.5
 cargo_planes_constraint_for_pair_BA_on_day_2: yBA2 - uBA2 <= 2.5
 cargo_planes_constraint_for_pair_BA_on_day_3: yBA3 - uBA3 <= 2.5
 cargo_planes_constraint_for_pair_BA_on_day_4: yBA4 - uBA4 <= 2.5
 cargo_planes_constraint_for_pair_BC_on_day_0: yBC0 - uBC0 <= 2.5
 cargo_planes_constraint_for_pair_BC_on_day_1: yBC1 - uBC1 <= 2.5
 cargo_planes_constraint_for_pair_BC_on_day_2: yBC2 - uBC2 <= 2.5
 cargo_planes_constraint_for_pair_BC_on_day_3: yBC3 - uBC3 <= 2.5
 cargo_planes_constraint_for_pair_BC_on_day_4: yBC4 - uBC4 <= 2.5
 cargo_planes_constraint_for_pair_CA_on_day_0: yCA0 - uCA0 <= 4
 cargo_planes_constraint_for_pair_CA_on_day_1: yCA1 - uCA1 <= 4
 cargo_planes_constraint_for_pair_CA_on_day_2: yCA2 - uCA2 <= 4
 cargo_planes_constraint_for_pair_CA_on_day_3: yCA3 - uCA3 <= 4
 cargo_planes_constraint_for_pair_CA_on_day_4: yCA4 - uCA4 <= 4
 cargo_planes_constraint_for_pair_CB_on_day_0: yCB0 - uCB0 <= 40
 cargo_planes_constraint_for_pair_CB_on_day_1: yCB1 - uCB1 <= 20
 cargo_planes_constraint_for_pair_CB_on_day_2: yCB2 - uCB2 <= 30
 cargo_planes_constraint_for_pair_CB_on_day_3: yCB3 - uCB3 <= 20
 cargo_planes_constraint_for_pair_CB_on_day_4: yCB4 - uCB4 <= 40
 wrap_around_cargo_flow_balance: yAB4 + uAB0 - uAB4 = 30
 wrap_around_cargo_flow_balance: yAC4 + uAC0 - uAC4 = 5
 wrap_around_cargo_flow_balance: yBA4 + uBA0 - uBA4 = 2.5
 wrap_around_cargo_flow_balance: yBC4 + uBC0 - uBC4 = 2.5
 wrap_around_cargo_flow_balance: yCA4 + uCA0 - uCA4 = 4
 wrap_around_cargo_flow_balance: yCB4 + uCB0 - uCB4 = 40
 wrap_around_planes_flow_balance_A: xAB0 + xAC0 - xBA4 - xCA4 + yAB0 + yAC0
   - yBA4 - yCA4 + zA0 - zA4 = 0
 wrap_around_planes_flow_balance_B: - xAB4 + xBA0 + xBC0 - xCB4 - yAB4
   + yBA0 + yBC0 - yCB4 + zB0 - zB4 = 0
 wrap_around_planes_flow_balance_C: - xAC4 - xBC4 + xCA0 + xCB0 - yAC4
   - yBC4 + yCA0 + yCB0 + zC0 - zC4 = 0
Bounds
End
