# Transcript: The Saved-Time Check, real run on a real case
Case: Koodo Mobile · Koodo Assist, signed out, 28 Oct 2026 (public test).
Run 15 Nov 2026: a fresh Claude agent given only this folder's SKILL.md played the skill; the user's turns use only the facts and quotes from the public test (see the `.case.md` file). Text below is verbatim; only the pace of the video is changed.

## User
We tested Koodo Mobile's assistant, Koodo Assist, on 28 October, signed out. Assistants like this are usually counted as time saved for the support team. Does a chat like ours count?

## Skill
**Saved-Time Check: Koodo Assist (signed-out chat, 28 October)**

Yes, I can check that. Since you tested it from the outside, the claim I'll check is the usual one for this kind of assistant: "each chat it handles is time our people don't spend." Koodo hasn't said that. It's just the claim these assistants usually get counted under.

What decides it is where your job ended up. Did the assistant finish it in the chat, hand it to a person, or leave it with you? Please tell me:

1. What did you ask Koodo Assist to do? Give the task in a sentence or two.
2. How did the chat end? Did it finish the job itself, pass you to a person (live agent, callback, form), or send you somewhere else to do it yourself (a link, an app, a store, "sign in to continue")?
3. If it passed you to a person, did you have to repeat any of what you'd already typed?
4. Which steps, if any, did it finish completely on its own?
5. Did you record anything from the test, like a transcript, screenshots or how long it took? Only real figures, no estimates.
6. Did you check any of Koodo's own published pages about the assistant or its support? If so, which ones?

"We don't know" is a fine answer to any of these. Some things can't be seen from outside, like Koodo's time records, staffing and usage data. I'll mark those "Not visible" and say what Koodo would need to check internally.

If you want help turning hours into results: an Executive Briefing, scalebotics.io

## User
1. Mobile data had stopped, but the phone showed bars and calls worked. What should I try first?
2. It gave the right steps: SIM card, cellular data, network reset, the APN, restart. Then we asked: if I connect to a rep, will I have to repeat all this, and how will I know someone has it? It asked us to sign in, which is fair for account help.
3. We asked first whether the rep would see this chat. It said: "I don't have enough information to confirm whether a representative receives the chat history or how the handoff is confirmed." We didn't sign in or reach a rep.
4. The troubleshooting steps. Whether they fixed the problem, the test can't show.
5. The transcript, dated 28 October. No timings.
6. Koodo's help pages say you get a text and an email when a rep replies, and messages are kept for up to 90 days. That answer never reached the chat. We can't see Koodo's time records, staffing or usage data.

Yes, please give me the one-page result too.

## Skill
**Saved-Time Check: Koodo Assist, mobile-data troubleshooting chat**
**Do the hours count as value? Not yet: the handoff is unclear.**
**What the hours are today:** Estimated capacity
The assistant couldn't say whether a rep sees the chat, so any chat that goes to a rep may make the customer repeat everything, and that adds time instead of saving it.

The claim checked is the usual one for this kind of assistant: "each chat it handles is time our people don't spend."

1. How was the time measured? Not visible
   What you have: A transcript of one test chat, dated 28 October, with no timings. Koodo's time records can't be seen from outside.
   To close the gap: Koodo would compare how long mobile-data contacts take to handle, before and after the assistant, from its own records.
2. What work was added? Partly
   What you have: A rep handoff needs you to sign in. The assistant said it doesn't have enough information to confirm whether a rep gets the chat history. Koodo's help pages say you get a text and an email when a rep replies, and that messages are kept for up to 90 days. That tells you how you'll hear back. It doesn't say whether the rep sees the chat, and that answer never reached the chat.
   To close the gap: Koodo would check whether reps get the chat history at handoff, and how long reps spend asking again.
3. Where did the capacity go? Not visible
   What you have: The assistant gave the right steps (SIM card, cellular data, network reset, APN, restart), but the test can't show whether they fixed the problem. If the job then goes to a rep, the work moves to that rep. Nothing is freed.
   To close the gap: Koodo would track how many mobile-data chats end without a rep, and where any freed rep time went.
4. Which outcome changed? Not visible
   What you have: The test can't show whether the steps fixed the problem.
   To close the gap: Koodo would compare repeat contacts and rep cases for mobile data, before and after the assistant.
Also ask: what does your usage data prove? Not visible
   What you have: Koodo's usage data can't be seen from a signed-out test.
   To close the gap: Koodo would check how much the assistant is used on mobile-data problems specifically, not overall chat counts.

**Next three actions**
1. Run the chat again signed in, connect to a rep, and write down anything you have to repeat.
2. Time the next test from the first message to the fix, the handoff, or the dead end.
3. Put the help pages' handoff answer next to the chat's "I don't have enough information" in your notes.

**The one-page result**

```json
{"tool": "saved-time-check", "view": "outside",
 "use": "Koodo Assist, mobile-data troubleshooting chat",
 "claim": "Each chat it handles is time our people don't spend. Gap: it can't say if a rep sees the chat.",
 "answer": "Not yet: the handoff is unclear",
 "source": "Signed-out Koodo Assist chat, mobile data issue, transcript dated 28 October",
 "parts": [
  {"status": "Not visible", "have": "Transcript of one test chat, 28 October. No timings. Koodo's time records can't be seen.", "close": "Koodo compares handling time for mobile-data contacts before and after the assistant."},
  {"status": "Partly", "have": "Rep handoff needs sign-in. Assist couldn't say if the rep sees the chat, so customers may repeat.", "close": "Koodo checks whether reps get the chat history, and times reps re-asking."},
  {"status": "Not visible", "have": "Right steps given, fix not confirmed. Chats that go to a rep move work; they don't free it.", "close": "Koodo tracks mobile-data chats that end without a rep, and where rep time went."},
  {"status": "Not visible", "have": "The test can't show whether the steps fixed the problem.", "close": "Koodo checks repeat contacts and rep cases for mobile data, before and after."},
  {"status": "Not visible", "have": "Koodo's usage data can't be seen from a signed-out test.", "close": "Koodo checks assistant use on mobile-data issues, not overall chat counts."}
 ],
 "actions": ["Re-run the chat signed in, connect to a rep, note anything you must repeat.", "Time the next test: first message to fix, handoff, or dead end.", "Put the help-page handoff answer next to the chat's 'not enough information.'"]}
```

If you want help turning hours into results: an Executive Briefing, scalebotics.io
