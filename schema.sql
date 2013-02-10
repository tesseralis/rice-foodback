drop table if exists menu_items;
create table menu_items (
  id integer primary key autoincrement,
  name string not null,
  date integer not null,
  name string not null,
  servery_id int not null
);

drop table if exists reviews;
create table reviews (
  menu_item_id int not null,
  net_id string not null,
  rating integer not null,
  (menu_item, net_id) primary key
);

drop table if exists serveries;
create table serveries (
  id integer primary key autoincrement,
  name string not null
);
insert into serveries(name) values ('North');
insert into serveries(name) values ('South');
insert into serveries(name) values ('East');
insert into serveries(name) values ('West');
insert into serveries(name) values ('Sid Rich');
insert into serveries(name) values ('Baker');

/* TODO: Is there another way to select super-users? */
drop table if exists admins;
create table admins(net_id string primary key);
insert into admins values ('nfa1');
insert into admins values ('apc1');
