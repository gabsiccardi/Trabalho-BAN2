PGDMP         0                z            Banco    14.2    14.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    24829    Banco    DATABASE     l   CREATE DATABASE "Banco" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United Kingdom.1252';
    DROP DATABASE "Banco";
                postgres    false            ?            1259    24869    atendimentos    TABLE     ?   CREATE TABLE public.atendimentos (
    nroatendimento integer NOT NULL,
    data date,
    cpfcliente numeric,
    matriculafuncionario integer,
    motivo text
);
     DROP TABLE public.atendimentos;
       public         heap    postgres    false            ?            1259    24868    atendimentos_nroAtendimento_seq    SEQUENCE     ?   CREATE SEQUENCE public."atendimentos_nroAtendimento_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."atendimentos_nroAtendimento_seq";
       public          postgres    false    213                       0    0    atendimentos_nroAtendimento_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public."atendimentos_nroAtendimento_seq" OWNED BY public.atendimentos.nroatendimento;
          public          postgres    false    212            ?            1259    24849    clientes    TABLE     ?   CREATE TABLE public.clientes (
    cpf numeric NOT NULL,
    nroagencia integer,
    nome text,
    cidade text,
    telefone text
);
    DROP TABLE public.clientes;
       public         heap    postgres    false            ?            1259    24893    contas    TABLE     ?   CREATE TABLE public.contas (
    nroconta integer NOT NULL,
    limite bigint NOT NULL,
    tipoconta integer,
    cpf numeric
);
    DROP TABLE public.contas;
       public         heap    postgres    false            ?            1259    24892    contas_nroconta_seq    SEQUENCE     ?   CREATE SEQUENCE public.contas_nroconta_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.contas_nroconta_seq;
       public          postgres    false    215                       0    0    contas_nroconta_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.contas_nroconta_seq OWNED BY public.contas.nroconta;
          public          postgres    false    214            ?            1259    24861    funcionarios    TABLE     ?   CREATE TABLE public.funcionarios (
    matricula integer NOT NULL,
    nome text,
    cpf numeric,
    salario numeric,
    funcao text
);
     DROP TABLE public.funcionarios;
       public         heap    postgres    false            ?            1259    24830 	   tipoconta    TABLE     v   CREATE TABLE public.tipoconta (
    codtipo integer NOT NULL,
    limitemaximo numeric NOT NULL,
    nometipo text
);
    DROP TABLE public.tipoconta;
       public         heap    postgres    false            m           2604    24872    atendimentos nroatendimento    DEFAULT     ?   ALTER TABLE ONLY public.atendimentos ALTER COLUMN nroatendimento SET DEFAULT nextval('public."atendimentos_nroAtendimento_seq"'::regclass);
 J   ALTER TABLE public.atendimentos ALTER COLUMN nroatendimento DROP DEFAULT;
       public          postgres    false    212    213    213            n           2604    24896    contas nroconta    DEFAULT     r   ALTER TABLE ONLY public.contas ALTER COLUMN nroconta SET DEFAULT nextval('public.contas_nroconta_seq'::regclass);
 >   ALTER TABLE public.contas ALTER COLUMN nroconta DROP DEFAULT;
       public          postgres    false    214    215    215                      0    24869    atendimentos 
   TABLE DATA           f   COPY public.atendimentos (nroatendimento, data, cpfcliente, matriculafuncionario, motivo) FROM stdin;
    public          postgres    false    213   ?"       	          0    24849    clientes 
   TABLE DATA           K   COPY public.clientes (cpf, nroagencia, nome, cidade, telefone) FROM stdin;
    public          postgres    false    210   ?"                 0    24893    contas 
   TABLE DATA           B   COPY public.contas (nroconta, limite, tipoconta, cpf) FROM stdin;
    public          postgres    false    215   l#       
          0    24861    funcionarios 
   TABLE DATA           M   COPY public.funcionarios (matricula, nome, cpf, salario, funcao) FROM stdin;
    public          postgres    false    211   ?#                 0    24830 	   tipoconta 
   TABLE DATA           D   COPY public.tipoconta (codtipo, limitemaximo, nometipo) FROM stdin;
    public          postgres    false    209   ?#                  0    0    atendimentos_nroAtendimento_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public."atendimentos_nroAtendimento_seq"', 1, false);
          public          postgres    false    212                       0    0    contas_nroconta_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.contas_nroconta_seq', 1, false);
          public          postgres    false    214            v           2606    24876    atendimentos atendimentos_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.atendimentos
    ADD CONSTRAINT atendimentos_pkey PRIMARY KEY (nroatendimento);
 H   ALTER TABLE ONLY public.atendimentos DROP CONSTRAINT atendimentos_pkey;
       public            postgres    false    213            r           2606    24855    clientes clientes_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (cpf);
 @   ALTER TABLE ONLY public.clientes DROP CONSTRAINT clientes_pkey;
       public            postgres    false    210            x           2606    24900    contas contas_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.contas
    ADD CONSTRAINT contas_pkey PRIMARY KEY (nroconta);
 <   ALTER TABLE ONLY public.contas DROP CONSTRAINT contas_pkey;
       public            postgres    false    215            t           2606    24867    funcionarios funcionarios_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (matricula);
 H   ALTER TABLE ONLY public.funcionarios DROP CONSTRAINT funcionarios_pkey;
       public            postgres    false    211            p           2606    24836    tipoconta tipoconta_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.tipoconta
    ADD CONSTRAINT tipoconta_pkey PRIMARY KEY (codtipo);
 B   ALTER TABLE ONLY public.tipoconta DROP CONSTRAINT tipoconta_pkey;
       public            postgres    false    209            {           2606    24901 
   contas cpf    FK CONSTRAINT     i   ALTER TABLE ONLY public.contas
    ADD CONSTRAINT cpf FOREIGN KEY (cpf) REFERENCES public.clientes(cpf);
 4   ALTER TABLE ONLY public.contas DROP CONSTRAINT cpf;
       public          postgres    false    215    210    3186            y           2606    24877    atendimentos cpfCliente    FK CONSTRAINT        ALTER TABLE ONLY public.atendimentos
    ADD CONSTRAINT "cpfCliente" FOREIGN KEY (cpfcliente) REFERENCES public.clientes(cpf);
 C   ALTER TABLE ONLY public.atendimentos DROP CONSTRAINT "cpfCliente";
       public          postgres    false    213    3186    210            z           2606    24882 !   atendimentos matriculaFuncionario    FK CONSTRAINT     ?   ALTER TABLE ONLY public.atendimentos
    ADD CONSTRAINT "matriculaFuncionario" FOREIGN KEY (matriculafuncionario) REFERENCES public.funcionarios(matricula);
 M   ALTER TABLE ONLY public.atendimentos DROP CONSTRAINT "matriculaFuncionario";
       public          postgres    false    211    213    3188            |           2606    24906    contas tipoconta    FK CONSTRAINT     z   ALTER TABLE ONLY public.contas
    ADD CONSTRAINT tipoconta FOREIGN KEY (tipoconta) REFERENCES public.tipoconta(codtipo);
 :   ALTER TABLE ONLY public.contas DROP CONSTRAINT tipoconta;
       public          postgres    false    3184    209    215               8   x?3453?4202?50?52?415?44?0?t,?M?+?WHIU????,I?????? ??i      	   t   x?342?4450?tOL*?L??????+???I?41??42?215???)ͬJD??0?2???441??s^???X???ihhia?eif?ifl?MN,?t?)?M?K,k63?????? 6j"?         +   x?3?4600?4?415?2?4q?8?-,?,?-!\?\? ?7?      
   F   x?34?0?tOL*?L??442?4500?tO-J?+I?2?05?H,???45326?4Js:'fV$r??qqq ?u8         )   x?3?4500?HL):?8?ˈ?? ?/J??,??????? ?	6     