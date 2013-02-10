drop table if exists menu_item;
create table menu_item (
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

insert into serveries(name) values ('north');
insert into serveries(name) values ('south');
insert into serveries(name) values ('east');
insert into serveries(name) values ('west');
insert into serveries(name) values ('sidrich');
insert into serveries(name) values ('baker');

drop table if exists admins;
create table admins(net_id string primary key);

insert into admins values ('nfa1');


