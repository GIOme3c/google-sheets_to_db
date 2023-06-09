PGDMP     
            
        {         	   test-task    15.2    15.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16413 	   test-task    DATABASE        CREATE DATABASE "test-task" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE "test-task";
                postgres    false            �            1255    16414    update_orders_price_usd()    FUNCTION     �   CREATE FUNCTION public.update_orders_price_usd() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  IF NEW.variable_name = 'usd_to_rub' THEN
    UPDATE orders
    SET price_rub = price_usd * NEW.variable_value;
  END IF;
  RETURN NULL;
END;
$$;
 0   DROP FUNCTION public.update_orders_price_usd();
       public          postgres    false            �            1255    16415    update_price_usd()    FUNCTION       CREATE FUNCTION public.update_price_usd() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  UPDATE orders
  SET price_rub = NEW.price_usd * (SELECT variable_value FROM local_variables WHERE variable_name = 'usd_to_rub')
  WHERE order_id = NEW.order_id;
  RETURN NEW;
END;
$$;
 )   DROP FUNCTION public.update_price_usd();
       public          postgres    false            �            1259    16416    local_variables    TABLE     �   CREATE TABLE public.local_variables (
    variable_name character(64) NOT NULL,
    variable_value double precision NOT NULL
);
 #   DROP TABLE public.local_variables;
       public         heap    postgres    false            �            1259    16419    orders    TABLE     �   CREATE TABLE public.orders (
    number bigint NOT NULL,
    order_id bigint NOT NULL,
    price_usd double precision NOT NULL,
    price_rub double precision,
    delivery_date date NOT NULL
);
    DROP TABLE public.orders;
       public         heap    postgres    false            �          0    16416    local_variables 
   TABLE DATA           H   COPY public.local_variables (variable_name, variable_value) FROM stdin;
    public          postgres    false    214   �       �          0    16419    orders 
   TABLE DATA           W   COPY public.orders (number, order_id, price_usd, price_rub, delivery_date) FROM stdin;
    public          postgres    false    215          k           2606    16423 $   local_variables local_variables_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.local_variables
    ADD CONSTRAINT local_variables_pkey PRIMARY KEY (variable_name);
 N   ALTER TABLE ONLY public.local_variables DROP CONSTRAINT local_variables_pkey;
       public            postgres    false    214            m           2606    16425    orders orders_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);
 <   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_pkey;
       public            postgres    false    215            n           2620    16432 /   local_variables update_orders_price_usd_trigger    TRIGGER     �   CREATE TRIGGER update_orders_price_usd_trigger AFTER UPDATE OF variable_value ON public.local_variables FOR EACH ROW EXECUTE FUNCTION public.update_orders_price_usd();
 H   DROP TRIGGER update_orders_price_usd_trigger ON public.local_variables;
       public          postgres    false    217    214    214            o           2620    16427    orders update_price_usd_trigger    TRIGGER        CREATE TRIGGER update_price_usd_trigger AFTER INSERT ON public.orders FOR EACH ROW EXECUTE FUNCTION public.update_price_usd();
 8   DROP TRIGGER update_price_usd_trigger ON public.orders;
       public          postgres    false    216    215            �   9   x�+-N�/ɏ/*MR pZꙛ�r%����$��M�N�#� CK�=... P��      �   O  x�uU[R9�N�B���]���X�a�LQ�G�0iے,��uR�H_�yd��"�۲�K�r	���#��{�u+���
�e]������G�Q����N>XZ�Q�>,o�޾88�s��Rs�n���h��0J ː��e' �k�bU<�����=a�K�n[a�\��DU��e7��p�)�5KM}۱o��h4}"%:`&�̠!@�-���2�e�@��3C�l����%pX��P|o�����T;�b���f�
L�J׮�z�f��o/<�!��.��ߢ�90LB
��Y>!�e��d4�������5�3�QdpC
?��$h9bT��Ҫ��@�8�6�-hd h
��C���Xj�jԨ�R:	Z^Bt�$ �4b�J���	���$���7YP5����ܪ�6E v^�Z� 9�ֱe4p+(��>�f�j��֨�ܕ#���I9X�~g#Ÿ�����Xd���)臻{!F�T���������?�6�2�k�RJ�X.S�|5v#����Ր܃ދ1��۰�5���
����4�B�D����:)c��2a��6u��3�H��<�#M ��{v�=.�Ic�(�fKD���4&�\'��f�Ǡ���ĳ;�1JF�:������G ���!ü�Y�Z�� @��0�!�'�O�����U#Z'B���!���f��j��>�N�|x˞������?�vݮAhC,|��w6�S��$�]dx�a9���036��)jA��B�	7�)���052�Y5�	IV#,�(|���(�Z�}���%�@�s��e��"U��\�\q����a5�W�.��*���rF�m����_;t\�     