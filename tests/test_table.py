import unittest
from unittest.mock import patch, MagicMock
from api.table import CounterTable
from azure.data.tables import TableServiceClient


class TestCounterTable(unittest.TestCase):
    @patch('api.table.TABLE_CONNECTION_STRING', new='fake_connection_string')
    @patch.object(TableServiceClient, 'from_connection_string', autospec=True)
    def test_increment(self, mock_from_connection_string):
        # Arrange
        self.counter_table = CounterTable()
        self.mock_table_service = MagicMock()
        self.mock_table_client = MagicMock()

        # mock TableServiceClient.from_connection_string context
        mock_tsc_context = mock_from_connection_string.return_value
        mock_enter_tsc = mock_tsc_context.__enter__
        # mock table_service
        mock_enter_tsc.return_value = self.mock_table_service

        # mock TableServiceClient.get_table_client
        mock_tc_context = self.mock_table_service.get_table_client
        mock_enter_tc = mock_tc_context.return_value.__enter__
        # mock table_client
        mock_enter_tc.return_value = self.mock_table_client

        # mock table_client.get_entity
        self.mock_table_client.get_entity.return_value = {"count": 1}

        # Act
        count = self.counter_table.increment()

        # Assert
        mock_from_connection_string.assert_called_once_with(
            conn_str='fake_connection_string'
        )
        self.mock_table_service.get_table_client.assert_called_once_with(
            "counter"
        )
        self.mock_table_client.get_entity.assert_called_once_with(
            "counter", "counter"
        )
        self.mock_table_client.update_entity.assert_called_once_with(
            entity={"count": 2}
        )
        self.assertEqual(count, 2)

    @patch('api.table.TABLE_CONNECTION_STRING', new='fake_connection_string')
    @patch.object(TableServiceClient, 'from_connection_string', autospec=True)
    def test_increment_no_counter(self, mock_from_connection_string):
        # Arrange
        self.counter_table = CounterTable()
        self.mock_table_service = MagicMock()
        self.mock_table_client = MagicMock()

        # mock TableServiceClient.from_connection_string context
        mock_tsc_context = mock_from_connection_string.return_value
        mock_enter_tsc = mock_tsc_context.__enter__
        # mock table_service
        mock_enter_tsc.return_value = self.mock_table_service

        # mock TableServiceClient.get_table_client
        mock_tc_context = self.mock_table_service.get_table_client
        mock_enter_tc = mock_tc_context.return_value.__enter__
        # mock table_client
        mock_enter_tc.return_value = self.mock_table_client

        # mock table_client.get_entity
        self.mock_table_client.get_entity.return_value = None

        # Act
        count = self.counter_table.increment()

        # Assert
        mock_from_connection_string.assert_called_once_with(
            conn_str='fake_connection_string'
        )
        self.mock_table_service.get_table_client.assert_called_once_with(
            "counter"
        )
        self.mock_table_client.get_entity.assert_called_once_with(
            "counter", "counter"
        )
        self.mock_table_client.create_entity.assert_called_once_with(
            entity={
                "PartitionKey": "counter",
                "RowKey": "counter",
                "count": 1
            }
        )
        self.assertEqual(count, 1)
