CREATE TABLE `design_claims` (
	`id` text PRIMARY KEY NOT NULL,
	`design_id` integer NOT NULL,
	`claim_text` text NOT NULL,
	`claim_type` text NOT NULL,
	`source_id` text,
	`status` text NOT NULL,
	FOREIGN KEY (`design_id`) REFERENCES `designs`(`id`) ON UPDATE no action ON DELETE no action,
	FOREIGN KEY (`source_id`) REFERENCES `sources`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE INDEX `idx_claims_design` ON `design_claims` (`design_id`);--> statement-breakpoint
CREATE TABLE `countries` (
	`id` text PRIMARY KEY NOT NULL,
	`name` text NOT NULL,
	`region` text
);
--> statement-breakpoint
CREATE UNIQUE INDEX `countries_name_unique` ON `countries` (`name`);--> statement-breakpoint
CREATE TABLE `designs` (
	`id` integer PRIMARY KEY NOT NULL,
	`selected_country_id` text,
	`inputs_json` text NOT NULL,
	`design_summary` text NOT NULL,
	`updated_at` text NOT NULL,
	FOREIGN KEY (`selected_country_id`) REFERENCES `countries`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE TABLE `events` (
	`id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	`user_id` text NOT NULL,
	`kind` text NOT NULL,
	`detail` text NOT NULL,
	`created_at` text NOT NULL
);
--> statement-breakpoint
CREATE INDEX `idx_events_user_time` ON `events` (`user_id`,`created_at`);--> statement-breakpoint
CREATE TABLE `rate_limits` (
	`user_id` text PRIMARY KEY NOT NULL,
	`window` integer NOT NULL,
	`count` integer NOT NULL
);
--> statement-breakpoint
CREATE TABLE `metrics` (
	`id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	`country_id` text NOT NULL,
	`metric_name` text NOT NULL,
	`value` real,
	`unit` text NOT NULL,
	`reporting_period` text NOT NULL,
	`source_id` text NOT NULL,
	`retrieved_at` text NOT NULL,
	`confidence` text,
	`notes` text,
	FOREIGN KEY (`country_id`) REFERENCES `countries`(`id`) ON UPDATE no action ON DELETE no action,
	FOREIGN KEY (`source_id`) REFERENCES `sources`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE INDEX `idx_metrics_country_metric` ON `metrics` (`country_id`,`metric_name`);--> statement-breakpoint
CREATE UNIQUE INDEX `idx_metrics_observation` ON `metrics` (`country_id`,`metric_name`,`reporting_period`,`retrieved_at`);--> statement-breakpoint
CREATE TABLE `sources` (
	`id` text PRIMARY KEY NOT NULL,
	`publisher` text NOT NULL,
	`title` text NOT NULL,
	`url` text NOT NULL,
	`source_type` text NOT NULL,
	`publication_date` text,
	`accessed_at` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `users` (
	`id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	`authenticated_user_id` text NOT NULL,
	`email` text,
	`role` text DEFAULT 'viewer' NOT NULL,
	`registered_at` text NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `users_authenticated_user_id_unique` ON `users` (`authenticated_user_id`);