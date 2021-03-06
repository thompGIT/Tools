PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE programs (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE question_categories (id INTEGER PRIMARY KEY, text TEXT);
CREATE TABLE questions (id INTEGER PRIMARY KEY, category NUMERIC, text TEXT, helptext TEXT);
CREATE TABLE reports (id INTEGER PRIMARY KEY, date TEXT, program INTEGER, pointsavailable INTEGER, pointsearned INTEGER);
CREATE TABLE surveys (id INTEGER PRIMARY KEY, date TEXT);
CREATE TABLE surveyresponses (id INTEGER PRIMARY KEY, survey INTEGER, question INTEGER, evaluator INTEGER, score INTEGER, notes TEXT);
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);

INSERT INTO question_categories (id,text) VALUES ( 1,'Cost');
INSERT INTO question_categories (id,text) VALUES ( 2,'CM');
INSERT INTO question_categories (id,text) VALUES ( 3,'Development');
INSERT INTO question_categories (id,text) VALUES ( 4,'Fac/Eqt');
INSERT INTO question_categories (id,text) VALUES ( 5,'Peer Reviews');
INSERT INTO question_categories (id,text) VALUES ( 6,'Requirements');
INSERT INTO question_categories (id,text) VALUES ( 7,'Risks');
INSERT INTO question_categories (id,text) VALUES ( 8,'Schedule');
INSERT INTO question_categories (id,text) VALUES ( 9,'Signoffs');
INSERT INTO question_categories (id,text) VALUES (10,'Staffing');
INSERT INTO question_categories (id,text) VALUES (11,'Test');
INSERT INTO question_categories (id,text) VALUES (12,'VR');

INSERT INTO questions (category, text, helptext) VALUES(8,'Were all milestones over last 3 months met on time? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(8,'On schedule per latest plan? ','(2-yes 1-behind no more than a week 0-behind more than a week)');
INSERT INTO questions (category, text, helptext) VALUES(1,'Is work accomplished to date in line with cost expended?','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(1,'Does remaining budget cover estimate to complete?','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(1,'Any large (>33%) changes in burn rate over next 3 months?','(2-no, 1-somewhat, 0-yes)');
INSERT INTO questions (category, text, helptext) VALUES(4,'Do you have adequate facilities & eqpt to perform to plan?','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(4,'Are there plans in place to address shortcomings in facilities & eqpt?','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(10,'Adequate staff to perform to plan? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(10,'Are staffing needs accurate in PeoplePower? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(7,'Are risks managed (identified, monitored, mitigations planned & executed)? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(7,'Have risks been briefed to COI leadership? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(12,'Were pubs/items delivered according to schedule ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(12,'Were pubs/items peer reviewed? ','(2-yes, 1-some, 0-none)');
INSERT INTO questions (category, text, helptext) VALUES(3,'Number of open bugs vs number of resolved bugs at the end of the Iteration? ','(2-shrinking, 1-steady, 0-growing)');
INSERT INTO questions (category, text, helptext) VALUES(3,'Was User Story ‘Done-ness’ criteria approved by the Customer for the last month? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(3,'Number of ‘total’ and ‘not-met’ user stories for features/bug fixes in the last completed iteration compared to total? ','(2-25% or less not met, 1-26% to 50% not met, 0-more than 50% not met)');
INSERT INTO questions (category, text, helptext) VALUES(3,'How were test cases determined for the last iteration? ','(2-well-thought out, 1-guessed, 0-didn''t have any to use)');
INSERT INTO questions (category, text, helptext) VALUES(6,'Have requirements been reviewed for testability? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(6,'Are there requirements that are outside the company''s scope of responsibility? ','(2-no, 1-somewhat, 0-yes)');
INSERT INTO questions (category, text, helptext) VALUES(6,'Have any requirements changed after SRR/approval? ','(2-ten or less, 1-ten to twenty, 0-more than twenty)');
INSERT INTO questions (category, text, helptext) VALUES(6,'Is the RTM/RVTM up to date with the latest requirements changes? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(5,'Are mgt plans being peer reviewed? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(5,'Are design artifacts being peer reviewed? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(5,'Is code being peer reviewed? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(5,'Are test plans/procedures peer reviewed? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(2,'Rework due to CM errors ?','(2-none, 1-some, 0-much or bad delivery to customer (beta or other))');
INSERT INTO questions (category, text, helptext) VALUES(11,'Has code been unit tested before handoff to test team? ','(2-yes, 1-somewhat, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(11,'Has I&T phase slipped (e.g. due to dev delays)? ','(2-no, 1-somewhat, 0-yes)');
INSERT INTO questions (category, text, helptext) VALUES(11,'Do test procedures cover all requirements? ','(2-yes, 1-mostly, 0-no)');
INSERT INTO questions (category, text, helptext) VALUES(11,'SW bugs found during Golden FAT?','(2-five or less, 1-six to twenty, 0-more than twenty)');
INSERT INTO questions (category, text, helptext) VALUES(11,'Number of known issues going into FAT? ','(2-five or less, 1-six to twenty, 0-more than twenty)');
INSERT INTO questions (category, text, helptext) VALUES(9,'Any security department concerns? ','(2-none, 1-some, 0-many)');
INSERT INTO questions (category, text, helptext) VALUES(9,'Any finance department concerns?  ','(2-none, 1-some, 0-many)');
INSERT INTO questions (category, text, helptext) VALUES(9,'Any mission excellence concerns (Test, QA, Tech Pubs, CM, Prop Mgt)?  ','(2-none, 1-some, 0-many)');
INSERT INTO questions (category, text, helptext) VALUES(9,'Any contracts department concerns? ','(2-none, 1-some, 0-many)');

COMMIT;
