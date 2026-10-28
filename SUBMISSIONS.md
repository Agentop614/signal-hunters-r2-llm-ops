# How each upload was produced

| Upload | Command | Validation (PKS-like v2) | Leaderboard |
| --- | --- | --- | --- |
| v6 | `python make_submission.py cache data/test_meta.csv submission_r2_v6.csv` | 0.8995 | 0.9003 |
| v8 | `FEATS=lvl,trk OUT=submission_r2_v8.csv python stacker/stack.py` | 0.9092 | 0.9044 |
| v9 | `INDIV=effb2_fixup2,effb0_fixup2,effb2_fix,effb0_fix,effb2_fixs2,effb0_fixs2,effb2_fix45,effb3_fix FSPLIT=trainpks2 FEATS=lvl,trk OUT=submission_r2_v9.csv python stacker/stack.py` | 0.9162 | — |

PKS-like v2 = Gamma k=12 receiver noise + per-panel gain offsets (std 0.13 of the noise scale), matched to the
panel-to-panel level spread measured on the test cadences. v8's stacker was trained on v1 features (no gain offsets).

v10 (adds notebook 5 = run 13, models effb2_up2s5/effb0_up2s5; validation PKS-like v2 0.9180):
`SPEC=effb2_fixup2:0.2,effb0_fixup2:0.2,effb2_up2s5:0.2,effb0_up2s5:0.2,effb2_fix:0.05,effb0_fix:0.05,effb2_fix45:0.05,effb3_fix:0.05 INDIV=effb2_fixup2,effb0_fixup2,effb2_up2s5,effb0_up2s5,effb2_fix,effb0_fix,effb2_fixs2,effb0_fixs2,effb2_fix45,effb3_fix FSPLIT=trainpks2 FEATS=lvl,trk OUT=submission_r2_v10.csv python stacker/stack.py`
(v9 leaderboard: 0.9158)

v11 (adds notebook 9 = run 17, models effb2_lvlfast/effb0_lvlfast; validation PKS-like v2 0.9307):
`SPEC=effb2_lvlfast:0.25,effb0_lvlfast:0.15,effb2_fixup2:0.15,effb0_fixup2:0.1,effb2_up2s5:0.15,effb0_up2s5:0.1,effb2_fix45:0.05,effb3_fix:0.05 INDIV=effb2_lvlfast,effb0_lvlfast,effb2_fixup2,effb0_fixup2,effb2_up2s5,effb0_up2s5,effb2_fix,effb0_fix,effb2_fixs2,effb0_fixs2,effb2_fix45,effb3_fix FSPLIT=trainpks2 FEATS=lvl,trk OUT=submission_r2_v11.csv python stacker/stack.py`
(v10 leaderboard: 0.9162)

v12 (adds notebooks 6 and 7 = runs 14 and 15; validation PKS-like v2 0.9364; v11 leaderboard 0.9257):
`SPEC=effb2_lvlup2:0.2,effb0_lvlup2:0.15,effb2_lvlpl3a:0.2,effb0_lvlpl3a:0.15,effb2_lvlfast:0.1,effb0_lvlfast:0.05,effb2_fixup2:0.05,effb2_up2s5:0.05,effb0_up2s5:0.05 INDIV=effb2_lvlup2,effb0_lvlup2,effb2_lvlpl3a,effb0_lvlpl3a,effb2_lvlfast,effb0_lvlfast,effb2_fixup2,effb0_fixup2,effb2_up2s5,effb0_up2s5 FSPLIT=trainpks2 FEATS=lvl,trk OUT=submission_r2_v12.csv python stacker/stack.py`

v14 (wave 2 = notebooks 11-13: runs 19/20/21, CNN v4 trained with real-PKS per-panel gain jitter; their oofpks use the honest v2 simulation):
1. `SPEC=effb0_pl4s1:0.25,effb0_pl4s2:0.25,effb0_pl4eti1:0.25,effb0_pl4eti2:0.25 INDIV=effb0_pl4s1,effb0_pl4s2,effb0_pl4eti1,effb0_pl4eti2 FSPLIT=trainpks2 FEATS=lvl,trk TAG=h20 python stacker/stack.py`  (honest validation 0.9295)
2. `SPEC=effb0_pl4s1:0.17,effb0_pl4s2:0.17,effb0_pl4eti1:0.16,effb0_pl4eti2:0.16,effb0_pl4c1:0.17,effb0_pl4c2:0.17 INDIV=effb0_pl4s1,effb0_pl4s2,effb0_pl4eti1,effb0_pl4eti2,effb0_pl4c1,effb0_pl4c2 FSPLIT=trainpks2 FEATS=lvl,trk TAG=v14a python stacker/stack.py`  (honest validation 0.9281)
3. v12 stacker as above with TAG=v12, then `python stacker/final_blend.py` -> submission_r2_v14_blend.csv = mean(v12, mean(h20, v14a)); submission_r2_v14_honest.csv = mean(h20, v14a).
(v12 leaderboard: 0.9285)
