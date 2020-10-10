--PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
--CREATE TABLE IF NOT EXISTS "cfc_app_law" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "summary" varchar(1000) NOT NULL, "impact_id" integer NULL REFERENCES "cfc_app_impact" ("id") DEFERRABLE INITIALLY DEFERRED, "location_id" integer NULL REFERENCES "cfc_app_location" ("id") DEFERRABLE INITIALLY DEFERRED, "key" varchar(20) NOT NULL UNIQUE);
INSERT INTO cfc_app_law (id, title, summary, impact_id, location_id, key) VALUES(1,'Provision of Tribal Healthcare Dental Services','Dental services for adults,  emergency dental care and extractions in an annual amount of not more than $1,000 per member.  When treated at an Indian Health Service or Tribal Facility, adult dental services that are eligible for a federal medical assistance percentage of 100% in excess of the limit prescribed.',1,5,'AZ-HB-2244 (2020)');
INSERT INTO cfc_app_law (id, title, summary, impact_id, location_id, key) VALUES(2,'Protection requirements for foster children','The results of background checks for each adult member of the foster care placement household will be used to determine danger level.  Foster children shall be kept safe from placements that constitute a Tier 5 danger. If the department determines that a placement constitutes a tier 5 danger, the department shall remove all foster children from this placement within four(24) hours after making the determination.',2,5,'AZ-SB-1682 (2020)');
INSERT INTO cfc_app_law (id, title, summary, impact_id, location_id, key) VALUES(3,'Establish state-wide standards for drinking water pollutants','Primary drinking water maximum contaminant levels established by the administrator before August 13, 1986 are adopted as drinking water aquifer water quality standards. The administrator may adopt additional primary drinking water maximum contaminant levels, unless "substantial opposition" are received during the first year of review.',3,5,'AZ-SB-1633 (2020)');
INSERT INTO cfc_app_law (id, title, summary, impact_id, location_id, key) VALUES(4,'Public airport fees prohibited for Ride Sharing companies','Additional or more restrictive requirements may not include a tax, fee or assessment of any kind on transportation network companies for operating at a public airport.  Transportation Network Companies include Taxis, Limousines and Ride Sharing companies.',4,5,'AZ-HB-2817 (2020)');
INSERT INTO cfc_app_law (id, title, summary, impact_id, location_id, key) VALUES(5,'Financial literacy training qualifies as a work activity','As a condition of eligibility for unemployment insurance cash assistance,  all recipients shall engage in work activities.  The department may allow a course in financial literacy and personal finance to qualify as a work activity.  These may include instruction on household cash management techniques, using checking and savings accounts, obtaining and using term and term credit or securing a loan or other term financing arrangements for high-cost items.',5,5,'AZ-HB-2695 (2020)');
COMMIT;
