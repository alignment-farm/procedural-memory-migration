# Fresh evaluation lock

Recorded after recipient calibration, before any seed 400–411 model task run.
The source bank is bank-v2; reconstruction-v2 has the identical source-v1 archive
hash. Recipient Qwen3 8B calibration finished: none 2/6, inherit 6/6, reconstruct
5/6. The implemented rule chose reconstruct for aggregate and exclusion, inherit
for temporal, as recorded in artifacts/policy-v2.json. That JSON and all calibration
outcomes are committed before final evaluation. No further bank or policy change.

Inspection clarification: the reconstructed temporal card contains literal 5,
but its observed calibration failure was an unadapted table name, not a wrong
cutoff. Recipient ordinary checking often repairs table-name substitutions;
failed attempts and checking costs remain included. Reconstruction is the same
recipient's independent build from the full common archive, with matching prompt
and budget. It is not claimed to be the best possible reconstruction system.

Run the previously planned 12 recipient evaluation tasks, seeds 400–411, with
none, unchanged inherit, and reconstruct. Reuse selected static-arm records for
the precommitted policy, paying all 18 calibration tasks and reconstruction.

A pre-evaluation addition strengthens PM1 identification: also run the SOURCE
model on the exact same 12 final tasks under none and unchanged inherit. This
adds 24 complete attempts, serially on the same resources, after the recipient
runs. It holds task facts, obligations, checker and artifact fixed across models,
instead of relying on the source's different acquisition sample. These extra
controls are research evaluation cost, never recipient deployment cost. They
cannot change the already locked recipient policy. This is a small paired
model control, not another search/factorial or a new acquisition revision.

Report whole-task success and costs, task-paired outcome changes, family-level
patterns, and all overhead. Report source-bank construction both separately and
in lifetime totals. Latency/compute/money are not interchangeable with token
counts. Evaluate the policy at the observed 12-task horizon and show any token-only
break-even projection with its same-mix/quality limitations. No significance or
cross-domain generalization claim from three repeated synthetic templates.

End this bounded phase on the observed explanatory result, regardless of which
arm wins. Broader scientific closure and publication acceptance are not claimed.
