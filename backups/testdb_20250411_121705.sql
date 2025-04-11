--
-- PostgreSQL database dump
--

-- Dumped from database version 17.3
-- Dumped by pg_dump version 17.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: a; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.a (
    id integer
);


ALTER TABLE public.a OWNER TO postgres;

--
-- Name: course; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.course (
    id integer NOT NULL,
    title character varying(80) NOT NULL,
    start_date date,
    duration integer
);


ALTER TABLE public.course OWNER TO postgres;

--
-- Name: course_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.course_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.course_id_seq OWNER TO postgres;

--
-- Name: course_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.course_id_seq OWNED BY public.course.id;


--
-- Name: enrollment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enrollment (
    date timestamp without time zone DEFAULT now() NOT NULL,
    student_id integer NOT NULL,
    course_id integer NOT NULL
);


ALTER TABLE public.enrollment OWNER TO postgres;

--
-- Name: student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student (
    id integer NOT NULL,
    first_name character varying(45) NOT NULL,
    last_name character varying(45) NOT NULL,
    email text NOT NULL
);


ALTER TABLE public.student OWNER TO postgres;

--
-- Name: student_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.student_id_seq OWNER TO postgres;

--
-- Name: student_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_id_seq OWNED BY public.student.id;


--
-- Name: course id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.course ALTER COLUMN id SET DEFAULT nextval('public.course_id_seq'::regclass);


--
-- Name: student id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student ALTER COLUMN id SET DEFAULT nextval('public.student_id_seq'::regclass);


--
-- Data for Name: a; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.a (id) FROM stdin;
293847
777
\.


--
-- Data for Name: course; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.course (id, title, start_date, duration) FROM stdin;
1	Data Analyst	2025-06-15	250
2	Deep Learning	2025-07-10	125
3	Machine Learning	2025-09-10	100
4	Full Stack Software Developer	2025-06-03	300
5	DevOps Software Engineer	2025-08-16	550
6	Data Engineering	2025-10-03	425
\.


--
-- Data for Name: enrollment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.enrollment (date, student_id, course_id) FROM stdin;
2025-05-19 07:21:59	2	3
2025-05-21 12:16:23	2	2
2025-06-10 14:25:09	3	5
2025-06-28 15:34:23	4	6
2025-07-22 11:00:07	2	3
2025-08-10 02:23:10	5	4
2025-08-25 20:01:25	3	6
2025-08-30 18:16:15	5	2
\.


--
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student (id, first_name, last_name, email) FROM stdin;
1	Daniel	Jones	daniel@jones.com
2	Dirk	Mayer	dirk@mayer.com
3	Megan	Johnson	megan@johnson.com
4	Anna	Stone	anna@hstone.com
5	Richard	Herrmann	megan@herrmann.com
\.


--
-- Name: course_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.course_id_seq', 6, true);


--
-- Name: student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_id_seq', 5, true);


--
-- Name: course course_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.course
    ADD CONSTRAINT course_pkey PRIMARY KEY (id);


--
-- Name: enrollment enrollment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enrollment
    ADD CONSTRAINT enrollment_pkey PRIMARY KEY (student_id, course_id, date);


--
-- Name: student student_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_email_key UNIQUE (email);


--
-- Name: student student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (id);


--
-- Name: enrollment enrollment_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enrollment
    ADD CONSTRAINT enrollment_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.course(id);


--
-- Name: enrollment enrollment_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enrollment
    ADD CONSTRAINT enrollment_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT USAGE ON SCHEMA public TO read_only;
GRANT USAGE ON SCHEMA public TO read_write;


--
-- Name: TABLE a; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.a TO read_only;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.a TO read_write;


--
-- Name: TABLE course; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.course TO read_only;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.course TO read_write;


--
-- Name: TABLE enrollment; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.enrollment TO read_only;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.enrollment TO read_write;


--
-- Name: TABLE student; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.student TO read_only;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.student TO read_write;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT SELECT ON TABLES TO read_only;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT SELECT,INSERT,DELETE,UPDATE ON TABLES TO read_write;


--
-- PostgreSQL database dump complete
--

